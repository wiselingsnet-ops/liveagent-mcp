
"""
MCP Servers Configuration
Add or remove MCP servers here to integrate them with your agent.
"""

from mcp_client.server import MCPServerSse

# List of MCP servers to integrate with the agent
MCP_SERVERS = [
    # LiveKit Docs - Documentation search
    MCPServerSse(
        params={
            "url": "https://docs.livekit.io/mcp",
            "timeout": 10,
            "sse_read_timeout": 300,
        },
        cache_tools_list=True,
        name="LiveKit Docs"
    ),
    
    # Filesystem - File system operations (self-hosted)
    MCPServerSse(
        params={
            "url": "http://0.0.0.0:3000/mcp",
            "timeout": 10,
            "sse_read_timeout": 300,
        },
        cache_tools_list=True,
        name="Filesystem"
    ),
    
    # Git - Git repository operations (self-hosted)
    MCPServerSse(
        params={
            "url": "http://0.0.0.0:3001/mcp",
            "timeout": 10,
            "sse_read_timeout": 300,
        },
        cache_tools_list=True,
        name="Git"
    ),
    
    # SQLite - SQLite database operations (self-hosted)
    MCPServerSse(
        params={
            "url": "http://0.0.0.0:3002/mcp",
            "timeout": 10,
            "sse_read_timeout": 300,
        },
        cache_tools_list=True,
        name="SQLite"
    ),
    
    # Time - Current time and timezone information (self-hosted)
    MCPServerSse(
        params={
            "url": "http://0.0.0.0:3003/mcp",
            "timeout": 10,
            "sse_read_timeout": 300,
        },
        cache_tools_list=True,
        name="Time"
    ),
    
    # Brave Search - Web search capabilities
    # Note: Requires API key from https://brave.com/search/api/
    # MCPServerSse(
    #     params={
    #         "url": "https://mcp.braveapis.com/mcp",
    #         "headers": {"X-Brave-Api-Key": "YOUR_BRAVE_API_KEY_HERE"},
    #         "timeout": 10,
    #         "sse_read_timeout": 300,
    #     },
    #     cache_tools_list=True,
    #     name="Brave Search"
    # ),
    
    # Fetch - Read web pages and extract content
    # Note: Requires self-hosted or third-party MCP server
    # MCPServerSse(
    #     params={
    #         "url": "http://localhost:3000/mcp",
    #         "timeout": 10,
    #         "sse_read_timeout": 300,
    #     },
    #     cache_tools_list=True,
    #     name="Fetch"
    # ),
    
    # Memory - Persistent agent memory
    # Note: Requires self-hosted MCP server
    # MCPServerSse(
    #     params={
    #         "url": "http://localhost:3100/mcp",
    #         "timeout": 10,
    #         "sse_read_timeout": 300,
    #     },
    #     cache_tools_list=True,
    #     name="Memory"
    # ),
    
    # Time - Current time and timezone information
    # Note: Requires self-hosted MCP server
    # MCPServerSse(
    #     params={
    #         "url": "http://localhost:3200/mcp",
    #         "timeout": 10,
    #         "sse_read_timeout": 300,
    #     },
    #     cache_tools_list=True,
    #     name="Time"
    # ),
    
    # Sequential Thinking - Enhanced reasoning capabilities
    # Note: Requires self-hosted MCP server
    # MCPServerSse(
    #     params={
    #         "url": "http://localhost:3300/mcp",
    #         "timeout": 10,
    #         "sse_read_timeout": 300,
    #     },
    #     cache_tools_list=True,
    #     name="Sequential Thinking"
    # ),
]

def get_mcp_servers():
    """Returns the list of configured MCP servers."""
    return MCP_SERVERS
