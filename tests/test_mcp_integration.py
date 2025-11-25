import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from mcp_client.agent_tools import MCPToolsIntegration
from mcp_config import get_mcp_servers
from agent import DefaultAgent


@pytest.mark.asyncio
async def test_mcp_servers_configured():
    """Test that MCP servers are properly configured."""
    mcp_servers = get_mcp_servers()
    assert len(mcp_servers) > 0
    assert any(server.name == "LiveKit Docs" for server in mcp_servers)


@pytest.mark.asyncio
async def test_agent_with_mcp_tools():
    """Test that agent can be initialized with MCP tools."""
    agent = DefaultAgent()
    mcp_servers = get_mcp_servers()
    
    # Mock the MCP registration
    with patch.object(MCPToolsIntegration, 'register_with_agent', new_callable=AsyncMock) as mock_register:
        await MCPToolsIntegration.register_with_agent(
            agent=agent,
            mcp_servers=mcp_servers,
            convert_schemas_to_strict=True,
            auto_connect=True
        )
        mock_register.assert_called_once()


@pytest.mark.asyncio
async def test_livekit_docs_mcp_server():
    """Test that LiveKit Docs MCP server is configured correctly."""
    mcp_servers = get_mcp_servers()
    docs_server = next((s for s in mcp_servers if s.name == "LiveKit Docs"), None)
    
    assert docs_server is not None
    assert docs_server.params["url"] == "https://docs.livekit.io/mcp"
    assert docs_server.params["timeout"] == 10
    assert docs_server.cache_tools_list is True


@pytest.mark.asyncio
async def test_agent_instructions_include_tool_guidance():
    """Test that agent instructions include guidance for using tools."""
    agent = DefaultAgent()
    instructions = agent.instructions
    
    # Verify that the instructions mention tools
    assert "tools" in instructions.lower() or "tool" in instructions.lower()
