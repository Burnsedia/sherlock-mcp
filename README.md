# Sherlock MCP Server

[![GitHub stars](https://img.shields.io/github/stars/Burnsedia/sherlock-mcp?style=social)](https://github.com/Burnsedia/sherlock-mcp)
[![GitHub issues](https://img.shields.io/github/issues/Burnsedia/sherlock-mcp)](https://github.com/Burnsedia/sherlock-mcp/issues)
[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://hub.docker.com/)

**FastMCP server integration for the Sherlock OSINT tool** – Seamlessly search social media accounts across 400+ platforms using the Model Context Protocol. Perfect for OSINT researchers, cybersecurity professionals, and AI assistants performing username enumeration and open-source intelligence gathering.

## Mission

This project is built with a commitment to finding truth and countering propaganda through ethical open-source intelligence. In an era of misinformation and digital manipulation, we believe in empowering investigators, journalists, and truth-seekers with transparent, verifiable tools for social media reconnaissance.

Our mission is to:
- **Promote Truthful Investigation**: Provide reliable tools for fact-checking and source verification
- **Counter Propaganda**: Enable systematic analysis of online narratives and account authenticity
- **Maintain Ethical Standards**: Ensure all usage aligns with privacy rights and responsible disclosure
- **Foster Transparency**: Open-source development for community scrutiny and improvement

*Read our full [Mission Statement](MISSION.md) for detailed principles and applications.*

## Features

- **Username Search**: Find social media profiles associated with a username
- **Structured Output**: Returns formatted results with site names, URLs, and existence status
- **Error Handling**: Graceful handling of missing dependencies, timeouts, and failures
- **Ethical Use**: Designed for responsible OSINT investigations
- **MCP Integration**: Native support for Model Context Protocol in AI workflows

## Demo

Experience the power of OSINT username searching with this MCP server. Connect to your favorite MCP-compatible AI assistant and query social media presence instantly.

*Placeholder for demo GIF or screenshot – coming soon!*

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

## Contributing

We welcome contributions to enhance this OSINT MCP server! Whether it's bug fixes, new features, or documentation improvements, your input helps the cybersecurity and AI communities.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## Ethical Considerations

This tool is designed for truth-seeking and countering propaganda, but with great power comes great responsibility. Always use ethically and legally.

### General Guidelines
- Use only for legitimate OSINT purposes
- Respect platform terms of service
- Be aware of privacy implications
- Consider rate limiting to avoid overwhelming services

### Countering Propaganda Best Practices
- **Cross-Reference Sources**: Verify account authenticity across multiple platforms
- **Check Creation Dates**: New accounts may indicate coordinated campaigns
- **Analyze Patterns**: Look for coordinated posting behaviors or similar content
- **Respect Privacy**: Focus on public information and avoid doxxing
- **Fact-Check Results**: Use additional verification tools for claims
- **Document Methodology**: Maintain transparency in investigative processes
- **Avoid Harm**: Do not use findings to harass or intimidate individuals

### Responsible Usage
- Obtain proper authorization for investigations
- Comply with local laws and regulations
- Use findings to promote truth and accountability
- Share results responsibly to avoid contributing to misinformation

## Troubleshooting

- **Sherlock not found**: Install with `pipx install sherlock-project`
- **Timeout errors**: Increase timeout in code or use smaller username sets
- **No results**: Username may not exist on searched platforms

## License

MIT License