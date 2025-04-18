from app.aea import mapping
from app.utils.doi import key_points

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="AER-MCP")

_journal_dict: dict = {
    "American Economic Review": "aer",
    "AER: Insight": "aeri",
    "AEJ: Applied Economics": "app",
    "AEJ: Economic Policy": "pol",
    "AEJ: Macroeconomics": "mac",
    "AEJ: Microeconomics": "mic",
}


# @mcp.tool()
# def journal_dict() -> dict:
#     """
#     Get journal list and the short code
#
#     Returns:
#         The content of journal in type of dict
#     """
#     return _journal_dict

@mcp.tool()
def aea_search(q: str, journal_list: list = None, max_search: int = None) -> dict:
    """
    Search from ARA Journal.

    Args:
        q (str):
            The question for search
        journal_list (list):
            The journal list which search from,
            The default is ['aer']
        max_search (int):
            The max search results of returns.
            Limits the total number of results across all journals and higher speed of run.

    Returns:
        The search result with dict type.

    Notes:
        Total optional of journal is listed in ['aer', 'aeri', 'app', 'pol', 'mac', 'mic']
        The journal short name stands the follow dictionary:
        {
            "American Economic Review": "aer",
            "AER: Insight": "aeri",
            "AEJ: Applied Economics": "app",
            "AEJ: Economic Policy": "pol",
            "AEJ: Macroeconomics": "mac",
            "AEJ: Microeconomics": "mic",
        }

    Examples:
        >>> aea_search("monetary policy")
        >>> aea_search("labor market", journal_list=["aer", "mac", "app"])
        >>> aea_search("skill and age", journal_list=["aer", "aeri"], max_search=30)
    """
    if journal_list is None:
        # journal_list = _journal_dict.values()
        journal_list = ["aer", "aeri"]

    _results: dict = {}
    _count = 0
    for journal in journal_list:
        _results[journal]: list = []
        j_con_doi_list: list = mapping.mapping(journal)().search(q=q)
        for doi in j_con_doi_list:
            if (key := key_points(doi)) is not None:
                _results[journal].append(key)
                _count += 1
            if _count > max_search:
                return _results

    return _results


if __name__ == "__main__":
    mcp.run(transport="stdio")
