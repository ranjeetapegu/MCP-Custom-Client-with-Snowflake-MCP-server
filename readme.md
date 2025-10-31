# MCP Client Setup Guide

Complete step-by-step guide for setting up a Model Context Protocol (MCP) client project.

**Reference**: https://modelcontextprotocol.io/docs/develop/build-client

## Prerequisites

1. **Mac OS** (tested on macOS)
2. **Python 3.10+** (required for MCP package compatibility)
3. **uv** (latest version) - Python package manager
4. Verify uv installation: `uv --version`

## Setup Steps

### Step 1: Create Project Directory
```bash
# Navigate to your workspace
cd /Users/rpegu/Documents/GenAI/MCP_client

# Initialize new project (if not exists)
uv init mcp-client
cd mcp-client
```

### Step 2: Fix Python Version Requirements
**Important**: The MCP package requires Python >=3.10, so update your `pyproject.toml`:

```toml
[project]
name = "mcp-client"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"  # Changed from >=3.9
dependencies = [
    "anthropic>=0.71.0",
    "mcp>=1.19.0",
    "python-dotenv>=1.1.1",
]
```


### Step 3: Set Python Version
```bash
# Pin Python version to avoid conflicts
uv python pin 3.10

# This creates/updates .python-version file
```

### Step 4: Create Virtual Environment
```bash
# Remove any existing environment
rm -rf .venv

# Create new environment with Python 3.10+
uv venv --python 3.10

# Activate virtual environment
source .venv/bin/activate

# Verify Python version
python --version  # Should show Python 3.10.x
```

### Step 5: Install Dependencies
```bash
# Install required packages
uv add mcp anthropic python-dotenv

# Or use sync to install from pyproject.toml
uv sync
```


## System Specifications Used
- **OS**: macOS (darwin 24.6.0)
- **Python**: 3.10.11
- **Package Manager**: uv
- **Shell**: /bin/zsh
