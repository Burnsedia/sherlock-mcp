# Contributing to Sherlock MCP Server

Thank you for your interest in contributing to the Sherlock MCP Server project! This open-source initiative integrates the powerful Sherlock OSINT tool with the Model Context Protocol, enabling seamless social media username searches for AI assistants and cybersecurity professionals.

## How to Contribute

### Reporting Bugs
- Use the [GitHub Issues](https://github.com/Burnsedia/sherlock-mcp/issues) page to report bugs
- Provide detailed steps to reproduce, expected vs. actual behavior, and your environment (Python version, OS, etc.)

### Suggesting Features
- Open a [GitHub Issue](https://github.com/Burnsedia/sherlock-mcp/issues) with the "enhancement" label
- Describe the feature, its use case, and potential implementation

### Code Contributions
1. **Fork and Clone**: Fork this repository and clone your fork locally
2. **Set Up Development Environment**:
   ```bash
   uv sync --extra dev
   ```
3. **Run Tests**: Ensure all tests pass before making changes
   ```bash
   uv run pytest
   ```
4. **Make Changes**: Create a feature branch and implement your changes
5. **Test Thoroughly**: Add tests for new functionality and verify existing tests still pass
6. **Commit and Push**: Use clear, descriptive commit messages
7. **Submit PR**: Create a pull request with a detailed description

### Development Guidelines

- **Code Style**: Follow PEP 8 standards
- **Documentation**: Update README and docstrings for any new features
- **Testing**: Maintain high test coverage; add tests for bug fixes and new features
- **Commit Messages**: Use conventional commits (e.g., `feat: add new tool`, `fix: resolve timeout issue`)

### Testing
- Run the full test suite: `uv run pytest`
- Test MCP integration manually with an MCP client
- Ensure Docker builds work: `docker build -t sherlock-mcp .`

### Documentation
- Keep README.md up-to-date with new features
- Add code comments for complex logic
- Update tool descriptions in the MCP server

## Code of Conduct

This project follows a standard code of conduct. Be respectful, inclusive, and collaborative. Harassment or discriminatory behavior will not be tolerated.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

If you have questions about contributing, open an issue or reach out via [GitHub Discussions](https://github.com/Burnsedia/sherlock-mcp/discussions).

Happy contributing! 🚀