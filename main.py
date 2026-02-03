import subprocess
import json
import tempfile
import os
from fastmcp import FastMCP

mcp = FastMCP(
    name="Sherlock MCP Server",
    instructions="Search for social media accounts by username across 400+ platforms using the Sherlock OSINT tool. Provide a username to find associated profiles.",
)


def search_username_impl(username: str) -> dict:
    """
    Search for social media accounts associated with a given username.

    Args:
        username: The username to search for across social networks.

    Returns:
        A dictionary containing found profiles and metadata.
        Format: {"found": [{"site": str, "url": str, "exists": bool}], "total_found": int, "error": str (if any)}
    """
    # Check if Sherlock is installed
    try:
        result = subprocess.run(
            ["sherlock", "--version"], capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            return {
                "found": [],
                "total_found": 0,
                "error": "Sherlock CLI not found. Install it with: pipx install sherlock-project",
            }
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return {
            "found": [],
            "total_found": 0,
            "error": "Sherlock CLI not found. Install it with: pipx install sherlock-project",
        }

    # Create a temporary file for JSON output
    with tempfile.NamedTemporaryFile(
        mode="w+", suffix=".json", delete=False
    ) as temp_file:
        temp_json_path = temp_file.name

    try:
        # Run Sherlock with JSON output
        cmd = ["sherlock", "--json", temp_json_path, username]
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=300
        )  # 5 min timeout

        if result.returncode != 0:
            return {
                "found": [],
                "total_found": 0,
                "error": f"Sherlock failed: {result.stderr.strip()}",
            }

        # Read and parse the JSON output
        with open(temp_json_path, "r") as f:
            data = json.load(f)

        # Extract results for the username
        user_data = data.get(username, {})
        found = []
        total_found = 0

        for site, info in user_data.items():
            if info.get("exists", False):
                found.append({"site": site, "url": info.get("url", ""), "exists": True})
                total_found += 1

        return {"found": found, "total_found": total_found, "error": None}

    except subprocess.TimeoutExpired:
        return {
            "found": [],
            "total_found": 0,
            "error": "Search timed out after 300 seconds",
        }
    except json.JSONDecodeError:
        return {
            "found": [],
            "total_found": 0,
            "error": "Failed to parse Sherlock output",
        }
    except Exception as e:
        return {"found": [], "total_found": 0, "error": f"Unexpected error: {str(e)}"}
    finally:
        # Clean up temp file
        if os.path.exists(temp_json_path):
            os.unlink(temp_json_path)


search_username = mcp.tool()(search_username_impl)


if __name__ == "__main__":
    mcp.run(transport="stdio")
