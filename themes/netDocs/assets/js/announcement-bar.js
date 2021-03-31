$(function() {

    var globalNav = $('.globalNav'),
        globalNavHeight = globalNav.outerHeight(),
        ctaAnnouncementBar,
        ctaAnnouncementBarHeight;
    
    setTimeout(function() {
        if($('.cta.announcement-bar').length) {
            ctaAnnouncementBar = $('.cta.announcement-bar'),
            ctaAnnouncementBarHeight = ctaAnnouncementBar.outerHeight();        
        }
    },20)

    $( window ).scroll(function() { // on Scroll
        if($('#product-nav').length) {
            if($('.cta.announcement-bar').length) {
                var snappTop = globalNavHeight + ctaAnnouncementBarHeight;
            }else {
                var snappTop = globalNavHeight;
            }
           
            if($(window).scrollTop() > snappTop) {
                $('.globalNav').addClass('out-of-view')
                $('#product-nav').addClass('snapp');
            }else {
                $('.globalNav').removeClass('out-of-view');
                $('#product-nav').removeClass('snapp');
            }
        }
    });


    ///////////////////////////////////////////
    // TOP ANNOUNCEMENT BAR //////////////////
    /////////////////////////////////////////

    // Create cookie. Expiration date is determined in Wagtail.
    function setdismissNvidiaAnnouncementBlogPost() {
        $.cookie('dismissNvidiaAnnouncementBlogPost', 'true', { expires: 5, path: '/' });
    }

    // Check if dismissNvidiaAnnouncementBlogPost cookie exists
    if ( !$.cookie('dismissNvidiaAnnouncementBlogPost') ) {    
        $('<div class="cta announcement-bar nvidia-green text-md-center d-block"> <a href="javascript:void(0)" class="close"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="svg replaced-svg"><defs><style>.a{fill:none;stroke:currentColor;stroke-linecap:round;stroke-linejoin:round;}</style></defs><title>close</title><line class="a" x1="0.5" y1="0.499" x2="23.5" y2="23.499"></line><line class="a" x1="23.5" y1="0.499" x2="0.5" y2="23.499"></line></svg></a> <p>Cumulus Networks is now NVIDIA&reg;. <a href="https://blogs.nvidia.com/blog/2020/06/16/cumulus-programming-networks/" target="_blank">Learn more</a></p></div>').insertAfter('.globalNav');
        $('head').append('<style>body{transition: all 0.5s; -webkit-transition: all 0.5s;}.globalNav{top: 0;}.globalNav.snapp {top: -48px;}.globalNav.snapp~.cta.announcement-bar {top: 77px}.globalNav.snapp~.cta.announcement-bar~.docs-wrapper .book-toc>.toc {top: 124px;} @media only screen and (max-width: 576px){ body{top: 125px;}}</style>');
        
    }

    // Close the announcement bar when the user hits the X button
    $('body').on('click','.cta.announcement-bar a.close', function(e){
        $('.cta.announcement-bar').css('top', '-60px');
        $('.docs-wrapper').css({marginTop: 125})
        $('.docs-home header + section').css('padding', '73px 0 120px');
        //$('.globalNav, body').css('top', '0');
        setdismissNvidiaAnnouncementBlogPost();
        e.preventDefault();
    });
});