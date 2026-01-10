FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl git && rm -rf /var/lib/apt/lists/*

# Install pipx and Sherlock
RUN pip install pipx && pipx install sherlock-project

# Install FastMCP
RUN pip install fastmcp

# Copy project files
COPY . /app
WORKDIR /app

# Run the MCP server
CMD ["python", "main.py"]