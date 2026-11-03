document.addEventListener("DOMContentLoaded", function() {

    /*
     * Sets up a web worker that runs the lunr search. If this fails (for example due to stricter permissions on local file:// origins
     * in Google Chrome) then the function rejects the returned promise and a same-thread search adapter needs to be set up.
     */
    function createSearchWorker() {
        return new Promise((resolve, reject) => {
            const searchWorkerTemplate = document.querySelector('#search-worker');
            const searchWorkerBlob = new Blob([searchWorkerTemplate.textContent]);
            const searchWorker = new Worker(URL.createObjectURL(searchWorkerBlob));

            searchWorker.addEventListener('message', (event) => {
                if (event.data.type === 'ready') {
                    resolve({
                        search: (query) => {
                            searchWorker.postMessage({
                                type: 'search-request',
                                query
                            });
                        },

                        onResult: (fn) => {
                            searchWorker.addEventListener('message', (event) => {
                                var message = event.data;
                                if (message.type === 'search-results') {
                                    fn(message.results, message.query);
                                }
                            })
                        }
                    })
                } else if (event.data.type === 'error-setup') {
                    reject();
                }
            })

            // send page url to the worker, for script loading
            let locationOrigin = window.location.protocol
                + "//"
                + window.location.hostname
                + (
                    window.location.port
                        ? ':' + window.location.port
                        : ''
                );
            var pageLocation = locationOrigin + window.location.pathname;
            var url = pageLocation.substr(0, pageLocation.lastIndexOf('/') + 1);
            searchWorker.postMessage({ type: "setup", baseUrl: url });
        });
    }

    function loadDeferredScript(path) {
        return new Promise((resolve, reject) => {
            try {
                let script = document.createElement('script');
                script.src = path;
                // defer loading so we don't block but keep script load order
                script.defer = true;
                script.onload = resolve;
                script.onerror = reject;
                document.body.append(script);
            } catch(e) {
                reject(e);
            }
        });
    }

    function loadLunrDependencies() {
        return Promise.all([
            loadDeferredScript('js/lunr.js'),
            loadDeferredScript('js/lunr-index.js'),
            loadDeferredScript('js/lunr-data.js'),
            loadDeferredScript('js/lunr-extras.js').catch(() => {/* optional, ignore error */}),
        ]);
    }

    /*
     * Tries to set up a web-worker backed search but falls back to same-thread search if this fails.
     */
    function createSearchAdapter() {
        return createSearchWorker()
            .catch(() => loadLunrDependencies().then(() => {
                // global `lunr` and `lunrIndex` variables are created by lunr dependencies loaded above
                const searchIndex = lunr.Index.load(lunrIndex);
                const resultListeners = [];

                return {
                    search: (query) => {
                        var searchHits = searchIndex.search(query);
                        var results = searchHits.map(function (result) {
                            return lunrData.filter(function (d) {
                                return d.id === result.ref;
                            })[0]
                        });
                        resultListeners.forEach((fn) => fn(results, query));
                    },
                    onResult: (fn) => {
                        resultListeners.push(fn);
                    }
                };
            }))
    }

    const searchInputField = document.querySelector('#search-textbox');
    const searchSuggestionResults = document.querySelector('#search-suggestion-container');

    const debounce = (func, timeout = 500) => {
        let timeoutId;
        return (...args) => {
            clearTimeout(timeoutId);
            timeoutId = setTimeout(() => {
                func(...args);
            }, timeout);
        };
    };


    createSearchAdapter().then((searchAdapter) => {
        if (searchInputField) {
            const processSearchInput = (query, searchWorker) => {
                if (query.length >= 1) {
                    searchWorker.search(query);
                } else {
                    populateSearchSuggestions([]);
                }
            }

            const debounceSearch = debounce(processSearchInput);
            searchInputField.addEventListener('input', (ev) => {
                const query = ev.target.value;
                debounceSearch(query, searchAdapter);
            }, false);

            // if we're on the search.html page we'll show the results directly in the result container instead of the dropdown
            const searchResultsContainer = document.querySelector('#search-results-container');
            const searchResultsTemplate = document.querySelector('#search-results-template');

            if (searchResultsContainer && searchResultsTemplate) {
                // populate the results on the dedicated search page
                function populateSearchResults(results, query) {
                    document.getElementById("query-value").textContent = query;

                    const resultCount = document.getElementById("result-count");
                    if(results.length === 0) {
                        resultCount.textContent = ' returned no results';
                    }
                    else {
                        resultCount.textContent = ' returned ' + results.length + ' results';
                    }
                    const searchResultLinks = results.map((result) => {
                        const resultItem = searchResultsTemplate.content.cloneNode(true);
                        const resultLink = resultItem.querySelector('h2').querySelector('a');
                        const resultParagraph = resultItem.querySelector('small');
                        resultLink.textContent = result.title;
                        resultLink.href = result.link;
                        const baseUrl = window.location.href.substring(0, window.location.href.lastIndexOf('/') + 1);

                        resultParagraph.appendChild(document.createTextNode(baseUrl+ result.link));
                        return resultItem;
                    });

                    searchResultsContainer.replaceChildren(...searchResultLinks);
                }

                searchAdapter.onResult(populateSearchResults);

                // on load check if there is a search query already and
                const params = new Proxy(new URLSearchParams(window.location.search), {
                    get: (searchParams, prop) => searchParams.get(prop),
                });
                let query = params.searchQuery;
                // check query integrity and send search request
                if (query && query.length >= 1) {
                    searchAdapter.search(query);
                } else {
                    populateSearchResults([]);
                }
            } else if (searchSuggestionResults) {

                function hideSearchSuggestions() {
                    searchSuggestionResults.classList.add('hidden');
                }

                function showSearchSuggestions() {
                    searchSuggestionResults.classList.remove('hidden');
                }

                function addResultsPageEntry() {
                    let href = "search.html?searchQuery=" + encodeURIComponent(searchInputField.value);
                    let searchResultsItem = document.createElement('div');
                    searchResultsItem.id = "see-all-results"
                    searchResultsItem.className = "exp-search-suggestion-option-container search-form-suggestion";
                    searchResultsItem.tabIndex = -1;
                    let searchResultsLink = document.createElement('a');
                    searchResultsLink.href = href;
                    searchResultsLink.className = "exp-search-suggestion-option search-form-suggestion search-suggestions-see-all-item";
                    searchResultsLink.text = "See all search results";
                    searchResultsItem.append(searchResultsLink);
                    searchSuggestionResults.append(searchResultsItem);
                }

                function populateSearchSuggestions(results) {
                    // map search results to DOM elements with links to the pages
                    const searchSuggestionTemplate = document.querySelector('#exp-search-suggestion-option-template');
                    const searchSuggestionLinks = results.slice(0, 3).map((result) => {
                        const resultItem = searchSuggestionTemplate.content.cloneNode(true);
                        const resultLink = resultItem.querySelector('a');
                        resultLink.textContent = result.title;
                        resultLink.href = result.link;
                        return resultItem;
                    });

                    searchSuggestionResults.replaceChildren(...searchSuggestionLinks);
                    if (searchSuggestionResults.firstElementChild) {
                        searchSuggestionResults.firstElementChild.tabIndex = 0;
                    }
                    addResultsPageEntry();
                }

                searchAdapter.onResult(populateSearchSuggestions);

                // calling preventDefault on the search result suggestion prevents the search input field from losing the focus
                // otherwise the blur event from that would close the search result dropdown before the click on the result registers
                searchSuggestionResults.addEventListener('mousedown', (event) => event.preventDefault(), false);

                searchSuggestionResults.addEventListener('mouseover', (ev) => {
                    if (ev.target.matches('.exp-search-suggestion-option')) {
                        selectSuggestion(
                            getActiveSearchSuggestionElement(),
                            ev.target.parentElement
                        );
                    }
                }, false);

                function selectSuggestion(previousActive, newActive) {
                    showSearchSuggestions();
                    if (previousActive && newActive) {
                        previousActive.tabIndex = -1;
                        newActive.tabIndex = 0;
                        newActive.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                    }
                }

                function getActiveSearchSuggestionElement() {
                    return searchSuggestionResults.querySelector('.exp-search-suggestion-option-container[tabindex = "0"]')
                        || searchSuggestionResults.firstElementChild;
                }

                // bind handlers for search input fields
                searchInputField.addEventListener('focus', showSearchSuggestions, false);
                searchInputField.addEventListener('blur', hideSearchSuggestions, false);


                // add keyboard navigation to search dropdown
                searchInputField.addEventListener('keydown', (event) => {
                    const activeElement = getActiveSearchSuggestionElement();

                    function selectNextSuggestion() {
                        selectSuggestion(activeElement, activeElement.nextElementSibling);
                    }

                    function selectPreviousSuggestion() {
                        selectSuggestion(activeElement, activeElement.previousElementSibling);
                    }

                    function navigateToActiveSuggestionPage() {
                        if (activeElement) {
                            const link = activeElement.querySelector('a');
                            if (link) {
                                link.click();
                            }
                        }
                    }

                    switch (event.key) {
                        case 'ArrowUp':
                            event.preventDefault();
                            selectPreviousSuggestion();
                            break;
                        case 'ArrowDown':
                            event.preventDefault();
                            selectNextSuggestion();
                            break;
                        case 'Enter':
                            event.preventDefault();
                            navigateToActiveSuggestionPage();
                            break;
                        case 'Escape':
                            event.preventDefault();
                            searchInputField.blur();
                            break;
                        default:
                            break;
                    }
                }, false);
            }
        }
    });

});
