
from fastmcp import FastMCP
from anyio import to_thread
from sherlock_project.sherlock import sherlock
from sherlock_project.sites import SitesInformation
from sherlock_project.notify import QueryNotifyPrint
from sherlock_project.result import QueryResult



mcp = FastMCP(name="Sherlock MCP Server")


def _search_username(username: str, sites=None) -> dict:
    if not username or not username.strip():
        return {
            "found": [],
            "total_found": 0,
            "error": "Invalid username",
        }

    sites_info = SitesInformation()

    # OPTIONAL: filter sites
    if sites:
        sites_info.sites = {
            name: site
            for name, site in sites_info.sites.items()
            if name in sites
        }

    query_notify = QueryNotifyPrint()

    results = sherlock(
        username,
        sites_info.sites,   # ✅ THIS IS THE FIX
        query_notify,
        timeout=10,
    )

    found = [
        {"site": site, "url": result.url_user}
        for site, result in results.items()
        if result.status == QueryResult.Status.CLAIMED
    ]

    return {
        "found": found,
        "total_found": len(found),
        "error": None,
    }

   
@mcp.tool()
async def search_username(username: str, sites=None) -> dict:
    return await to_thread.run_sync(_search_username, username, sites)


if __name__ == "__main__":
    mcp.run(transport="stdio")

