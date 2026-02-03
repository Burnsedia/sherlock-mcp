from fastmcp import FastMCP
from sherlock.sherlock import sherlock
from sherlock.result import QueryResult


mcp = FastMCP(
    name="Sherlock MCP Server",
    instructions="Search for social media accounts by username across 400+ platforms using the Sherlock OSINT tool. Provide a username to find associated profiles.",
)

@mcp.tool()
def search_username(username: str, sites: list[str] | None = None) -> dict:
    """
    Pure Python Sherlock adapter.
    No MCP. No FastAPI. No subprocess.
    """

    results = sherlock(
        username=username,
        site_list=sites,
        timeout=10,
        print_all=False,
        color=False,
        verbose=False,
    )

    found = []

    for site, result in results.items():
        if result.status == QueryResult.Status.CLAIMED:
            found.append(
                {
                    "site": site,
                    "url": result.url_user,
                    "exists": True,
                }
            )

    return {
        "found": found,
        "total_found": len(found),
        "error": None,
    }



if __name__ == "__main__":
    mcp.run(transport="stdio")
