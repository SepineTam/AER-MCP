# AER-MCP

A MCP Server for finding from AEA.

> 🔍 Search papers from AEA with LLM
> 
> 🛠️ Still Under Developing
> 
> 💡 Inspiration: [arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)

## 💡 Quickly Start
### Localization
```bash
git clone https://github.com/sepinetam/aer-mcp.git
cd aer-mcp
uv venv .venv
```

Then, config it
```json
{
  "mcpServers": {
    "aer-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/the/repo/",
        "run",
        "aer_mcp.py"
      ]
    }
  }
}
```

## ⛓️ More Academic MCP Servers
- [Stata-MCP](https://github.com/sepinetam/stata-mcp)
- [NBER-MCP](https://github.com/sepinetam/nber-mcp)
- [arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)


