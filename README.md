# Sherlock MCP Server

A Model Context Protocol (MCP) server that integrates the [Sherlock](https://github.com/sherlock-project/sherlock) OSINT CLI tool, allowing AI assistants to search for social media accounts by username across 400+ platforms.

## Features

- **Username Search**: Find social media profiles associated with a username
- **Structured Output**: Returns formatted results with site names, URLs, and existence status
- **Error Handling**: Graceful handling of missing dependencies, timeouts, and failures
- **Ethical Use**: Designed for responsible OSINT investigations

## Prerequisites

- Python 3.13+
- Sherlock CLI tool installed: `pipx install sherlock-project`

## Docker Setup

For containerized deployment using the official Sherlock Docker image:

1. Build the Docker image:
   ```bash
   docker build -t sherlock-mcp .
   ```

2. Run the container:
   ```bash
   docker run -it sherlock-mcp
   ```

This starts the MCP server inside the container. Connect MCP clients via stdio pipes or configure HTTP transport for remote access.

## Installation

1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd sherlock-mcp
   ```

2. Install dependencies:
   ```bash
   pip install -e .
   ```

3. Ensure Sherlock is installed:
   ```bash
   pipx install sherlock-project
   ```

## Usage

### Running the Server

```bash
python main.py
```

This starts the MCP server with stdio transport, ready for MCP clients.

### Example MCP Client Usage

When connected to an MCP-compatible client (e.g., Claude Desktop), use the `search_username` tool:

```
Tool: search_username
Arguments: {"username": "exampleuser"}
```

Response:
```json
{
  "found": [
    {"site": "github", "url": "https://github.com/exampleuser", "exists": true},
    {"site": "twitter", "url": "https://twitter.com/exampleuser", "exists": true}
  ],
  "total_found": 2,
  "error": null
}
```

## Tool Reference

### `search_username(username: str)`

Searches for social media accounts associated with the given username.

**Parameters:**
- `username` (str): The username to search for

**Returns:**
- `found` (list): Array of found profiles with site, URL, and exists status
- `total_found` (int): Number of profiles found
- `error` (str): Error message if any (null on success)

## Ethical Considerations

- Use only for legitimate OSINT purposes
- Respect platform terms of service
- Be aware of privacy implications
- Consider rate limiting to avoid overwhelming services

## Troubleshooting

- **Sherlock not found**: Install with `pipx install sherlock-project`
- **Timeout errors**: Increase timeout in code or use smaller username sets
- **No results**: Username may not exist on searched platforms

## License

MIT License