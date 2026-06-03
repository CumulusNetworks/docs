#!/usr/bin/env python3
'''
This script will pull the collection of release note JSON files.

The script will parse and markdown sanatize the JSON.

And write markdown files for hugo to render into the respective product and version directories.

This will also write the XML files that are used to generate xls files for the release notes.
'''

from operator import itemgetter
import re
import requests
from distutils.version import LooseVersion

def get_json(product, version, json_file):
    '''
    Downloads the json file for a given product/version from the cloudfront bucket.
    Also sort based on "ticket" value.

    product - either "cl" or "netq"
    version - the specific version of file to download. For example, "3.2.1" or "4.1.1"
    json_file - either "fixed" or "affects"
    '''

    session = requests.Session()
    url = "https://d2whzysjlaya8k.cloudfront.net/{}/{}/{}.json".format(product, version, json_file)
    response = session.get(url)
    if response.status_code != 200:
        print('Unable to download {}. \nReceived response {}'.format(url, response.status_code))
        exit(1)

    return sorted(response.json(), key=itemgetter("ticket"), reverse=True)

def product_string(product):
    '''
    Take in the product short hand and return the product name.

    product - one of "cl" or "netq"
    '''
    if product == "cl":
        return "Cumulus Linux"
    elif product == "netq":
        return "Cumulus NetQ"
    else:
        print("Unknown product {}".format(product))
        exit(1)

def rn_location(product, version):
    '''
    Deals with the fact sometimes we move the location of RNs.
    All the exception cases of what product+version for the rn file location should live here.

    Takes in a product_string() and version_string()

    Returns:
    string path of rn file location
    '''
    directory = get_hugo_folder(product, version)

    # NetQ moved the location of the RN file in 3.2 and later.
    if product == "netq" and version_string(version) in ["2.4", "3.0", "3.1"]:
        return "content/{}/More-Documents/rn.md".format(directory)
    else:
        return "content/{}/Whats-New/rn.md".format(directory)

def version_string(version):
    '''
    Take in the semver product version and return just the major.minor

    version - product version string, like 3.0.0 or 4.1.4
    Return
     3.0
     4.1
    '''
    if version.count(".") == 1:
        return version

    # The rfind here will drop the right most value. This means 3.7.14.2 returns "3.7.14".
    # But we only want "3.7"
    while version.count(".") > 1:
        version = version[:version.rfind(".")]

    return version

def get_hugo_folder(product, version):
    '''
    Take in a product like "cl" and version string like "4.0.0"

    Returns
    Hugo /content directory name, for example cumulus-linux-40
    '''
    folder_ver = version_string(version).replace(".", "")

    if product == "cl":
        return "cumulus-linux-{}".format(folder_ver)
    elif product == "netq":
        return "cumulus-netq-{}".format(folder_ver)
    else:
        print("ERROR: Unknown product {}".format(product))
        exit(1)

def add_code_markdown(input_string, tag_to_replace):
    '''
    Replaces a generic tag with a <pre></pre> code block.
    This should be used for matching tags that do not indicate an open or close.

    For example:
    {noformat}
    this is some code
    {noformat}

    The requirement of a pair prevents a simple string.replace()

    Inputs:
        input_string - The string to search and replace on
        tag_to_replace - String representation of what to replace (e.g., "{noformat}")
    Returns:
        Updated string with the given tag replaced with open/closing <pre> tags
    '''
    matches = re.finditer(tag_to_replace, input_string)

    close_noformat = False
    for match in matches:
        if close_noformat:
            tag = "</pre>"
            close_noformat = False
        else:
            tag = "<pre>"
            close_noformat = True

        input_string = input_string.replace(tag_to_replace, tag, 1)

    return input_string

def sanatize_rn_for_markdown(string):
    '''
    Strip any special or problematic characters from the a string.
    This (generally) will be used on the release note text to strip characters that break markdown.

    string - The string to sanatize
    '''

    # # Remove HTML tags
    output_string = string.replace("<p>", "")
    output_string = output_string.replace("</p>", "")

    output_string = output_string.replace("`", "'")

    # Fix code blocks
    output_string = add_code_markdown(output_string, "{noformat}")
    output_string = add_code_markdown(output_string, "{code}")

    # Replace and clean up line returns
    output_string = output_string.replace("\r\n", "<br />")
    output_string = output_string.replace("\n ", "<br />")
    output_string = output_string.replace(".\n", "<br />")
    output_string = output_string.replace("\n", "")

    output_string = output_string.replace("&lt;", "<")
    output_string = output_string.replace("&gt;", ">")

    output_string = output_string.replace("<tt>", "`")
    output_string = output_string.replace("</tt>", "`")

    #Replace @ characters to prevent auto email link creation
    output_string = output_string.replace("@", "&#64;")
    output_string = output_string.replace("[", "&#91;")
    output_string = output_string.replace("]", "&#93;")

    #CM-21678
    output_string = output_string.replace('<div class=\"preformatted\" style=\"border-width: 1px;\"><div class=\"preformattedContent panelContent\"><pre>', "<br /><pre>")
    output_string = output_string.replace('<div class=\"code panel\" style=\"border-width: 1px;\"><div class=\"codeContent panelContent\">', '<br /><pre>')
    output_string = output_string.replace('<pre class=\"code-java\">', "")
    output_string = output_string.replace('<span class=\"code-keyword\">', "")
    output_string = output_string.replace("</span>", "")
    output_string = output_string.replace("</pre>\n</div></div>", "</pre><br />")

    # This is later due to other cleanups needing to run first
    output_string = output_string.replace("\r", "")

    # Escape pipe characters
    output_string = output_string.replace("|", "\|")

    # NetQ-5774 Fix. The use of "<>" in a string inside a code (<pre>) block disappears
    output_string = output_string.replace("<ipaddr>", "\<ipaddr\>")

    # NETQ-7489 Fix. Similar to above
    output_string = output_string.replace("<cloud-appliance-IP-address>", "\<cloud-appliance-IP-address\>")
    output_string = output_string.replace("<default/mgmt>", "\<default/mgmt\>")
    output_string = output_string.replace("<customer-premise>", "\<customer-premise\>")
    output_string = output_string.replace("<customer-email-address>", "\<customer-email-address\>")
    output_string = output_string.replace("<password>", "\<password\>")
    output_string = output_string.replace("<opid-here>", "\<opid-here\>")

    # Special Linux command, CM-29033
    output_string = output_string.replace("&amp;&amp;", "&&")

    # Formatting due to JIRA to Redmine migration
    output_string = output_string.replace("{{", "<code>")
    output_string = output_string.replace("}}", "</code>")

    return output_string

def sanatize_rn_for_xls(string):
    '''
    Strip any special or problematic characters from the a string.
    This (generally) will be used on the release note text to strip characters that break markdown.

    string - The string to sanatize
    '''

    # # Remove HTML tags
    # TAG_RE = re.compile(r'<[^>]+>')
    # output_string = TAG_RE.sub('', string)
    output_string = string.replace("<p>", "\015")
    output_string = output_string.replace("</p>", "")
    output_string = output_string.replace("<br>", "\015")
    output_string = output_string.replace("<br />", "\015")

    output_string = output_string.replace("&", "&amp;")
    output_string = output_string.replace("`", "&apos;")
    output_string = output_string.replace("\\<", "&lt;")
    output_string = output_string.replace("\\>", "&gt;")
    output_string = output_string.replace("<", "&lt;")
    output_string = output_string.replace(">", "&gt;")

    output_string = output_string.replace("&lt;tt&gt;", "")
    output_string = output_string.replace("&lt;/tt&gt;", "")

    output_string = output_string.replace("&lt;pre&gt;", "")
    output_string = output_string.replace("&lt;/pre&gt;", "")
    output_string = output_string.replace("&lt;pre class=\"code-java\"&gt;", "")

    output_string = output_string.replace('&lt;div class=\"code panel\" style=\"border-width: 1px;\"&gt;&lt;div class=\"codeContent panelContent\"&gt;', "")
    output_string = output_string.replace('&lt;div class=\"preformatted\" style=\"border-width: 1px;\"&gt;&lt;div class=\"preformattedContent panelContent\"&gt;', "")
    output_string = output_string.replace("&lt;/div&gt;", "")
    output_string = output_string.replace("&lt;span class=\"code-keyword\"&gt;", "")
    output_string = output_string.replace("&lt;/span&gt;", "")

    # NetQ-5774 Fix. The use of "<>" in a string inside a code (<pre>) block disappears
    output_string = output_string.replace("&lt;ipaddr&gt;", "[ipaddr]")

    output_string = output_string.replace("{noformat}", "")
    return output_string

def format_ticket_for_display(ticket):
    """
    ticket may be a single Redmine/Jira id or a comma-separated list.
    Returns plain ids, comma-separated when there is more than one.
    """
    if ticket is None or not str(ticket).strip():
        return ""
    parts = [p.strip() for p in str(ticket).split(",") if p.strip()]
    if not parts:
        return ""
    return ", ".join(parts)

# Product versions to skip entirely in the release notes build (see main()).
# No JSON download, no markdown/XLS tables, no per-version headers for these releases.
# Key: product short name ("cl" or "netq"). Value: full version strings to skip.
EXCLUDED_VERSIONS = {
    "cl": ["5.15.2", "5.16.2", "5.16.3", "5.16.4", "5.17.0"],
    "netq": ["2.4.0", "2.4.1", "3.0.0", "3.1.0", "3.2.0", "3.2.1", "3.3.0", "3.3.1", "4.0.0", "4.0.1", "4.1.0", "4.1.1", "4.2.0", "4.3.0", "4.4.0", "4.4.1", "4.5.0", "4.6.0", "4.7.0", "4.8.0", "5.0.0", "5.0.1", "5.2.0", "5.2.1"],
}

# Product versions still built, but omitted from Affects / Fixed columns (see
# filter_version_list_for_display): singles removed, ranges split around them.
# Key: product short name ("cl" or "netq"). Value: full version strings to hide.
HIDDEN_VERSIONS = {
    "cl": ["5.15.2", "5.16.2", "5.16.3", "5.16.4", "5.17.0"],
    "netq": [],
}

# Matches a single range token "lo-hi" (one hyphen between two version strings).
_VERSION_RANGE_RE = re.compile(r"^(.+?)-(.+)$")


def _loose_le(a, b):
    return LooseVersion(a) <= LooseVersion(b)


def _loose_lt(a, b):
    return LooseVersion(a) < LooseVersion(b)


def _sort_versions_ascending(versions):
    return sorted(versions, key=LooseVersion)


def _next_canonical_strictly_after(v, canonical_releases):
    '''
    Smallest shipping release strictly greater than v, from the JSON
    release_notes list (sorted ascending). Used to advance past a hidden version
    without inventing patch numbers that never shipped.
    '''
    if not canonical_releases:
        return None
    for c in canonical_releases:
        if _loose_lt(v, c):
            return c
    return None


def _numeric_tuple_from_version(v):
    '''
    Parse dot-separated numeric version into ints, or None if any segment is non-numeric.
    Used only for boundary arithmetic when splitting ranges at hidden versions.
    '''
    parts = v.split(".")
    out = []
    for p in parts:
        if not p.isdigit():
            return None
        out.append(int(p))
    return out


def _format_numeric_tuple(nums):
    return ".".join(str(n) for n in nums)


def _pred_numeric_dot_version(v):
    '''
    Strictly smaller neighbor for dot-numeric versions by "decrement" rules:
    5.16.2 -> 5.16.1; 5.16.0 -> 5.15.0; 5.0.0 -> 4.0.0.
    No synthetic high patch suffixes (e.g. never 5.15.999).
    Returns None if no predecessor (e.g. 0.0.0) or non-numeric token.
    '''
    nums = _numeric_tuple_from_version(v)
    if not nums:
        return None
    i = len(nums) - 1
    while i >= 0:
        if nums[i] > 0:
            nums[i] -= 1
            for j in range(i + 1, len(nums)):
                nums[j] = 0
            return _format_numeric_tuple(nums)
        i -= 1
    return None


def _succ_version_exclusive_lower_bound(v):
    '''
    Smallest numeric version strictly greater than v (increment last segment).
    '''
    nums = _numeric_tuple_from_version(v)
    if not nums:
        return None
    nums[-1] += 1
    return _format_numeric_tuple(nums)


def _succ_numeric_release(v):
    '''
    Next version in x.y.z space for walking a span: bump patch; when patch would
    exceed 99 roll to the next minor (5.15.99 -> 5.16.0). Used when no explicit
    literal caps the segment.
    '''
    nums = _numeric_tuple_from_version(v)
    if not nums or len(nums) < 2:
        return _succ_version_exclusive_lower_bound(v)
    if len(nums) >= 3:
        a, b, c = nums[0], nums[1], nums[2]
        if c < 99:
            return "{}.{}.{}".format(a, b, c + 1)
        if b < 99:
            return "{}.{}.0".format(a, b + 1)
        return "{}.0.0".format(a + 1)
    a, b = nums[0], nums[1]
    if b < 99:
        return "{}.{}".format(a, b + 1)
    return "{}.0".format(a + 1)


def _literal_strings_from_version_arrays(*arrays):
    '''
    Version endpoints explicitly present in affects/fixed arrays (singles and
    range endpoints, including comma-separated clauses). Used to cap segment
    highs when splitting so we prefer literals already in the source row.
    '''
    found = set()
    for arr in arrays:
        if not arr:
            continue
        for cell in arr:
            for clause in re.split(r",\s*", str(cell)):
                clause = clause.strip()
                if not clause:
                    continue
                m = _VERSION_RANGE_RE.match(clause)
                if m:
                    found.add(m.group(1).strip())
                    found.add(m.group(2).strip())
                else:
                    found.add(clause)
    return found


def _greatest_version_strictly_below_e(cursor, e, hi, literals, canonical_releases):
    '''
    Upper end of [cursor, end] with end < e (LooseVersion), end <= hi.
    Prefer actual shipping releases from release_notes_and_license_list.json
    (canonical_releases, sorted ascending); then literals from the ticket row; then numeric
    predecessor of e; finally synthetic patch walk if canonical_releases is None or empty.
    '''
    if not (_loose_lt(cursor, e) and _loose_le(cursor, hi)):
        return None

    if canonical_releases:
        pool = [
            v for v in canonical_releases
            if _loose_le(cursor, v) and _loose_lt(v, e) and _loose_le(v, hi)
        ]
        if pool:
            return max(pool, key=LooseVersion)

    pool = [
        v for v in literals
        if _loose_le(cursor, v) and _loose_lt(v, e) and _loose_le(v, hi)
    ]
    if pool:
        return max(pool, key=LooseVersion)

    pe = _pred_numeric_dot_version(e)
    if pe is not None and _loose_le(cursor, pe) and _loose_lt(pe, e):
        end = pe
        if _loose_lt(hi, end):
            end = hi
        return end if _loose_le(cursor, end) else None

    t = cursor
    for _ in range(5000):
        if not _loose_lt(t, e):
            break
        st = _succ_numeric_release(t)
        if st is None:
            return t if _loose_le(t, hi) and _loose_lt(t, e) else None
        if not _loose_lt(st, e):
            return t if _loose_le(t, hi) else None
        if _loose_lt(hi, st):
            return t if _loose_le(t, hi) else None
        t = st
    return t if _loose_le(t, hi) and _loose_lt(t, e) else None


def _format_span(lo, hi):
    if lo == hi:
        return lo
    return "{}-{}".format(lo, hi)


def _split_range_removing_hidden(lo, hi, hidden_set, literals, canonical_releases):
    '''
    Return a list of display tokens (single version or "lo-hi") covering
    [lo, hi] minus any version in hidden_set that lies in [lo, hi], inclusive.
    Segment upper bounds prefer shipping releases (canonical_releases from
    release_notes in release_notes_and_license_list.json); advancing past a
    hidden release uses the next shipping version, not invented patch numbers.
    '''
    if _loose_lt(hi, lo):
        return []

    bad = sorted(
        [e for e in hidden_set if _loose_le(lo, e) and _loose_le(e, hi)],
        key=LooseVersion,
    )
    if not bad:
        return [_format_span(lo, hi)]

    out = []
    cursor = lo
    for e in bad:
        if _loose_lt(e, cursor):
            continue
        if _loose_lt(cursor, e):
            end = _greatest_version_strictly_below_e(
                cursor, e, hi, literals, canonical_releases
            )
            if end is not None and _loose_le(cursor, end):
                out.append(_format_span(cursor, end))
        nxt = None
        if canonical_releases:
            nxt = _next_canonical_strictly_after(e, canonical_releases)
        if nxt is None:
            nxt = _succ_version_exclusive_lower_bound(e)
        if nxt is None:
            return out
        cursor = nxt
        if _loose_lt(hi, cursor):
            return out

    if _loose_le(cursor, hi):
        out.append(_format_span(cursor, hi))
    return out


def _filter_one_version_token(token, hidden_set, literals, canonical_releases):
    '''
    token is one entry from affects_versions / fixed_versions (possibly after splitting on commas).
    '''
    token = token.strip()
    if not token:
        return []
    if token in hidden_set:
        return []

    m = _VERSION_RANGE_RE.match(token)
    if not m:
        return [token]

    lo, hi = m.group(1).strip(), m.group(2).strip()
    if not lo or not hi:
        return [token]
    return _split_range_removing_hidden(
        lo, hi, hidden_set, literals, canonical_releases
    )


def _dedupe_version_tokens_preserve_order(tokens):
    '''
    Multiple JSON array entries (often overlapping affects/fixed ranges) can filter
    to identical display fragments; keep first occurrence, drop repeats.
    '''
    seen = set()
    out = []
    for t in tokens:
        if t in seen:
            continue
        seen.add(t)
        out.append(t)
    return out


def _version_display_sort_key(token):
    '''
    Sort key for ascending display: by span start (lo), then span end (hi),
    using LooseVersion. Singles use the same version for lo and hi.
    '''
    tok = (token or "").strip()
    if not tok:
        return (LooseVersion("0"), LooseVersion("0"))
    m = _VERSION_RANGE_RE.match(tok)
    if m:
        lo, hi = m.group(1).strip(), m.group(2).strip()
        return (LooseVersion(lo), LooseVersion(hi))
    return (LooseVersion(tok), LooseVersion(tok))


def filter_version_list_for_display(
        product, version_list, literal_pool=None, canonical_releases=None):
    '''
    Drop hidden product versions from display strings. Splits inclusive ranges
    around hidden versions; also splits comma-separated clauses inside one string.

    literal_pool - optional set of version strings from the same ticket row
    (typically affects + fixed) used to choose upper bounds when splitting; if
    omitted, only endpoints parsed from version_list are used.

    canonical_releases - optional sorted ascending list of all shipping versions for this
    product from release_notes in release_notes_and_license_list.json; when set,
    segment bounds and "next after hidden" use only that catalog first.

    Output clauses are deduplicated then sorted ascending by range start (then end),
    so order does not depend on JSON array/clause ordering or how ranges were split.
    '''
    if not version_list:
        return version_list
    hidden = frozenset(HIDDEN_VERSIONS.get(product, []))
    if not hidden:
        return version_list

    literals = (
        _literal_strings_from_version_arrays(version_list)
        if literal_pool is None
        else set(literal_pool)
    )

    out = []
    for cell in version_list:
        if cell is None:
            continue
        s = str(cell).strip()
        if not s:
            continue
        # Same delimiter style as rendered output: comma + space between clauses
        for clause in re.split(r",\s*", s):
            clause = clause.strip()
            if not clause:
                continue
            out.extend(
                _filter_one_version_token(
                    clause, hidden, literals, canonical_releases
                )
            )
    deduped = _dedupe_version_tokens_preserve_order(out)
    return sorted(deduped, key=_version_display_sort_key)


def build_rn_markdown(json_file, version, file_type, product, canonical_releases=None):
    '''
    Builds a list of lines that contain the entire formatted release notes in markdown table format.

    json_file - the json output to parse and build release notes from
    version - a full version string, i.e., 3.7.11
    file_type - one of "affects" or "fixed"
    product - short name "cl" or "netq" (filters HIDDEN_VERSIONS from Affects/Fixed columns)
    canonical_releases - sorted ascending list from release_notes (same JSON as get_products);
        when provided, range splitting uses only shipping versions from that catalog first.
    '''
    output = []

    if file_type == "affects":
        output.append("### Open Issues in {}".format(version))
        output.append("\n")
        # output.append("<div class=\"table-wrapper\" markdown=\"block\">")
        output.append("\n")
        output.append("|  Issue ID 	|   Description	|   Affects	|   Fixed |")
        output.append("\n")
        output.append("|---	        |---	        |---	    |---	                |")
        output.append("\n")
    else:
        output.append("### Fixed Issues in {}".format(version))
        # output.append("<div class=\"table-wrapper\" markdown=\"block\">")
        output.append("\n")
        output.append("|  Issue ID 	|   Description	|   Affects	|")
        output.append("\n")
        output.append("|---	        |---	        |---	    |")
        output.append("\n")

    '''
    Generic JSON format is
    {
        "ticket": "2556037"  (or comma-separated ids, e.g. "2885305, 2887500, ..."),
        "jira_ticket": "CM-33012",
        "affects_versions": [
        "3.7.9-4.2.0"
        ],
        "release_notes_text": "After you add an interface to the bridge, an OSPF session flap can occur.\r\n\r\n"
    }
    '''
    for bug in json_file:
        '''
        With the conversion from Jira to Redmine the JSON file is now inconsistent.
        "ticket" may be a Jira CM or Redmine issue number, or a comma-separated list of numbers.
        The field "jira_ticket" is the Jira CM number, but not every issue has a mapped Jira ticket.
        '''
        issue_id_string = "| " + format_ticket_for_display(bug["ticket"]) + " | "
        raw_affects = bug.get("affects_versions") or []
        raw_fixed = bug.get("fixed_versions") or []
        row_literals = _literal_strings_from_version_arrays(raw_affects, raw_fixed)
        affects_display = filter_version_list_for_display(
            product, raw_affects, row_literals, canonical_releases
        )

        if file_type == "affects":
            fixed_display = filter_version_list_for_display(
                product, raw_fixed, row_literals, canonical_releases
            )
            output.append(
                issue_id_string
                + sanatize_rn_for_markdown(bug["release_notes_text"])
                + " | "
                + ", ".join(affects_display)
                + " | "
                + ", ".join(fixed_display)
                + "|"
            )
        else:
            output.append(
                issue_id_string
                + sanatize_rn_for_markdown(bug["release_notes_text"])
                + " | "
                + ", ".join(affects_display)
                + " | "
                + "|"
            )

        output.append("\n")

    # output.append("</div>")
    output.append("\n")

    return output

def build_markdown_header(product, version):
    '''
    Produce the hugo front matter for the release note file

    product - the product_string output, i.e., "Cumulus Linux"
    version - the Major.Minor release version, i.e., "4.0"
    '''
    if product == "Cumulus Linux":
        weight = "-30"
    elif product == "Cumulus NetQ":
        weight = "30"
    output = []

    output.append("---\n")
    output.append("title: NVIDIA {} {} Release Notes\n".format(product, version))
    output.append("author: Cumulus Networks\n")
    output.append("weight: {}\n".format(weight))
    output.append("product: {}\n".format(product))
    output.append("version: \"{}\"\n".format(version))
    output.append("toc: 1\n")
    output.append("type: rn\n")
    output.append("pdfhidden: True\n")
    output.append("---\n")
    output.append("\n\n")

    return output

def read_markdown_header(product, version):
    '''
    To allow for the modification of front matter within the release note files
    we will read in the existing front matter and use that instead of generating it manually.

    This will rely on a valid YAML closing "---" line as a delimiter

    product - the product_string output, i.e., "Cumulus Linux"
    version - the Major.Minor release version, i.e., "4.0"

    Returns a list of strings that are the existing front matter.
    '''

    input_file = rn_location(product, version)

    look_for_end_of_header = True
    header_lines = []
    with open(input_file, "r") as in_file:
        # skip the first line, it should be just a yaml header of "---"
        header_lines.append(in_file.readline())
        while look_for_end_of_header:
            current_line = in_file.readline()
            if current_line.strip("\n") == "---":
                look_for_end_of_header = False
                break
            header_lines.append(current_line)

        header_lines.append("---\n")
    return header_lines

def write_rns(output, file_type, product, version):
    '''
    Write the RN output to the file for a given version.

    output - a list of lines to write
    type - xls or md
    version - the version to write to in hugo directory syntax. For example, cumulus-linux-40
    '''

    directory = get_hugo_folder(product, version)
    if file_type not in ["xls", "md"]:
        print("Incorrect filetype. Can not write release notes.")
        exit(1)

    # DocRaptor requires the file to be an .xml file
    # but calling it xml when we are building xls is confusing
    if file_type == "xls":
        file_type = "xml"
        # this keeps the .xml file at the root of the version.
        # Moving it into the product specific folder makes generating xls much more complicated.
        output_file = "content/{}/rn.{}".format(directory, file_type)

    else:
        output_file = rn_location(product, version)

    with open(output_file, "w+") as out_file:
        for line in output:
            out_file.write(line)


def build_rn_markdown_files(product, version_list, canonical_releases=None):
    '''
    Build the contents of the markdown files for each version's release notes.
    This includes making the call to write the output to a file.

    This takes place for every version provided in version_list.

    product - The product to to generate markdown down. One of ['cl', 'netq']
    version_list - a list of all x.y.z release numbers to build release notes for
    canonical_releases - sorted ascending list from get_products()/release_notes
        (full product list); passed through for Affects/Fixed column filtering.
    '''
    files = ["affects", "fixed"] # Order matters. This order determines the order rendered on the RN page.

    # Sort the lists based on semver, most recent first.
    # I don't know what this does but that's what Stackoverflow is for
    # https://stackoverflow.com/a/2574090
    #version_list.sort(key=lambda s: list(map(int, s.split('.'))), reverse=True)
    version_list.sort(key=LooseVersion, reverse=True)
    # We need to map major.minors to full release list,
    # { 3.7: [3.7.1, 3.7.2, 3.7.3...]
    major_minor = {}

    for version in version_list:
        if version_string(version) in major_minor:
            major_minor[version_string(version)].append(version)
        else:
            major_minor[version_string(version)] = [version]

    # Now we have a map of majors.minors to ordered list of maintenance releases
    # loop over every major and build the RN page for that major
    for major in major_minor.keys():
        version_output = []

        # We only want to generate the frontmatter once per minor
        #version_output.extend(build_markdown_header(product_string(product), major))
        try:
            version_output.extend(read_markdown_header(product, major))
        except FileNotFoundError:
            version_output.extend(build_markdown_header(product_string(product), major))
        hugo_dir = get_hugo_folder(product, major)
        version_output.append("{{{{<rn_xls_link dir=\"{}\" >}}}}\n".format(hugo_dir))


        # Loop over all the maintenance releases.
        for version in major_minor[major]:
            print("Building markdown for {} {}\n".format(product_string(product), version))
            version_output.append("## {} Release Notes\n".format(version))

            # once for affects, once for fixed.
            for rn_file in files:
                version_output.extend(
                    build_rn_markdown(
                        get_json(product, version, rn_file),
                        version,
                        rn_file,
                        product,
                        canonical_releases,
                    )
                )

        # The version_output now contains the RNs for all maintenance releases in order.
        # Write out the markdown file.
        write_rns(version_output, "md", product, version)

def build_rn_xls(json_file, version, file_type, product, canonical_releases=None):
    '''
    This is a helper function to build_rn_xls_files().

    Given a maintenance version and file type it will generate an HTML table for that single combo.

    json_file - the json output to parse and build release notes from
    version - a full version string, i.e., 3.7.11
    product - short name "cl" or "netq" (used to filter HIDDEN_VERSIONS from Affects/Fixed columns)
    file_type - one of "affects" or "fixed"
    '''
    output = []
    if file_type == "affects":
        output.append("<table name=\"Open Issues in {}\">\n".format(version))
    else:
        output.append("<table name=\"Fixed Issues in {}\">\n".format(version))
    output.append("<tr>\n")
    output.append("<th> Issue ID </th>\n")
    output.append("<th> Description </th>\n")
    output.append("<th> Affects </th>\n")
    if file_type == "affects":
        output.append("<th> Fixed </th>\n")
    output.append("</tr>\n")
    for bug in json_file:
        rn_text = sanatize_rn_for_xls(bug["release_notes_text"])
        raw_affects = bug.get("affects_versions") or []
        raw_fixed = bug.get("fixed_versions") or []
        row_literals = _literal_strings_from_version_arrays(raw_affects, raw_fixed)
        affects_versions = filter_version_list_for_display(
            product, raw_affects, row_literals, canonical_releases
        )
        affects_str = ", ".join(affects_versions)
        if file_type == "affects":
            fixed_versions = filter_version_list_for_display(
                product, raw_fixed, row_literals, canonical_releases
            )
            fixed_str = ", ".join(fixed_versions)
        else:
            fixed_str = ""

        output.append("<tr>\n")
        output.append("<td>{}</td>\n".format(format_ticket_for_display(bug["ticket"])))
        output.append("<td>{}</td>\n".format(rn_text))
        output.append("<td>{}</td>\n".format(affects_str))
        if file_type == "affects":
            output.append("<td>{}</td>\n".format(fixed_str))
        output.append("</tr>\n")
    output.append("</table>\n")

    return output

def build_rn_xls_files(product, version_list, canonical_releases=None):
    '''
    This works in conjuction with build_rn_xls().

    This is responsible for putting together the entire HTML table.
    This includes putting all maintenance releases into a single table
    and building the tables for both "affects" and "fixed" notes.

    Whereas build_rn_xls() is only responsible for generating a table
    for a single table of (maintenance, [affects | fixed])

    This function will write the final file that can be consumed by DocRaptor to generate the xls file.
    '''
    files = ["affects", "fixed"]

    # Sort the lists based on semver, most recent first.
    # I don't know what this does but that's what Stackoverflow is for
    # https://stackoverflow.com/a/2574090
    #version_list.sort(key=lambda s: list(map(int, s.split('.'))), reverse=True)
    version_list.sort(key=LooseVersion, reverse=True)
    # We need to map major.minors to full release list,
    # { 3.7: [3.7.1, 3.7.2, 3.7.3...]
    major_minor = {}

    for version in version_list:
        if version_string(version) in major_minor:
            major_minor[version_string(version)].append(version)
        else:
            major_minor[version_string(version)] = [version]

    # Now we have a map of majors.minors to ordered list of maintenance releases
    # loop over every major and build the RN page for that major
    for major in major_minor.keys():

        # all_versions_xls is the combined table of all minors within a major in a single xls file.
        all_versions_xls = []

        all_versions_xls.append("<tables>\n")

        # Loop over all the maintenance releases.
        for version in major_minor[major]:
            print("Building xls for {} {}\n".format(product_string(product), version))

            # once for affects, once for fixed.
            for rn_file in files:
                rn_output = build_rn_xls(
                    get_json(product, version, rn_file),
                    version,
                    rn_file,
                    product,
                    canonical_releases,
                )
                all_versions_xls.extend(rn_output)

        # The one_version_output now contains the RNs for all maintenance releases in order.
        # Write out the markdown file.
        all_versions_xls.append("</tables>")
        write_rns(all_versions_xls, "xls", product, major)

def get_products():
    '''
    Download the engineering provided JSON file detailing the list of products and releases.
    Expects the key "release_notes" to exist at the top level.

    Returns: a dict of product short name and versions. For example
    { "cl":  ["3.7.1", "3.7.2"], "netq": ["2.4.0", "2.4.1", "3.0.0", "3.1.0"] }

    The same release list (sorted ascending by LooseVersion) is passed through
    to filter_version_list_for_display so Affects/Fixed range bounds use shipping
    versions from this file only (see release_notes_and_license_list.json).
    '''
    session = requests.Session()
    url = "https://d2whzysjlaya8k.cloudfront.net/release_notes_and_license_list.json"
    response = session.get(url)
    if response.status_code != 200:
        print("Unable to download JSON releases file to determine products and versions for release notes.")
        print('Received response {} from {}'.format(response.status_code, url))
        exit(1)

    if not "release_notes" in response.json():
        print("Unable to find release notes within JSON releases file. JSON dump:")
        print(response.json())
        exit(1)

    return response.json()["release_notes"]

def main():
    """
    Main function.
    """

    print("Fetching product and version list")
    products = get_products()

    for product in products:
        excluded = EXCLUDED_VERSIONS.get(product, [])
        hidden = HIDDEN_VERSIONS.get(product, [])
        version_list = [v for v in products[product] if v not in excluded]
        canonical_releases = _sort_versions_ascending(products[product])
        if excluded:
            print("Excluding {} versions from build: {}".format(product, excluded))
        if hidden:
            print("Hiding {} versions in Affects/Fixed columns: {}".format(product, hidden))
        build_rn_markdown_files(product, version_list, canonical_releases)
        build_rn_xls_files(product, version_list, canonical_releases)
    exit(0)


if __name__ == "__main__":
    main()
