#!/usr/bin/env python3
"""
Simple test script to verify MCP integration with the agent.
This script verifies the agent is configured and ready for testing.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

LIVEKIT_URL = os.getenv("LIVEKIT_URL", "")
LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY", "")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET", "")


def test_agent_mcp():
    """Verify agent MCP configuration."""
    
    print("🔧 Verifying Agent MCP Configuration")
    print("=" * 50)
    
    # Check credentials
    print("\n✓ LiveKit Credentials:")
    if LIVEKIT_URL:
        print(f"  ✅ URL: {LIVEKIT_URL}")
    else:
        print("  ❌ URL missing")
        return False
    
    if LIVEKIT_API_KEY:
        print(f"  ✅ API Key: {LIVEKIT_API_KEY[:8]}...")
    else:
        print("  ❌ API Key missing")
        return False
    
    if LIVEKIT_API_SECRET:
        print(f"  ✅ API Secret: {LIVEKIT_API_SECRET[:8]}...")
    else:
        print("  ❌ API Secret missing")
        return False
    
    # Check MCP configuration
    print("\n✓ MCP Configuration:")
    try:
        from mcp_config import get_mcp_servers
        mcp_servers = get_mcp_servers()
        print(f"  ✅ {len(mcp_servers)} MCP servers configured:")
        for server in mcp_servers:
            print(f"     - {server.name}")
    except Exception as e:
        print(f"  ❌ Error loading MCP config: {e}")
        return False
    
    # Check agent code
    print("\n✓ Agent Code:")
    try:
        from agent import DefaultAgent
        agent = DefaultAgent()
        if "LiveKit" in agent.instructions or "tools" in agent.instructions:
            print("  ✅ Agent instructions include MCP/tool guidance")
        else:
            print("  ⚠️  Agent instructions may not mention tools")
    except Exception as e:
        print(f"  ❌ Error loading agent: {e}")
        return False
    
    # Check tests
    print("\n✓ Tests:")
    if os.path.exists("tests/test_mcp_integration.py"):
        print("  ✅ MCP integration tests exist")
    else:
        print("  ⚠️  No MCP integration tests found")
    
    print("\n" + "=" * 50)
    print("✅ Agent is fully configured and ready for testing!")
    print("\n📝 To test the agent on LiveKit Cloud:")
    print("  1. Go to: https://cloud.livekit.io/")
    print("  2. Open your 'oyatalk' project")
    print("  3. Click on the agent or use the Sandbox")
    print("  4. Ask questions like:")
    print("     • 'Tell me about the LiveKit turn detector'")
    print("     • 'How do I use MCP servers with LiveKit agents?'")
    print("     • 'What are the latest LiveKit features?'")
    print("  5. Verify the agent mentions searching documentation")
    
    return True


if __name__ == "__main__":
    result = test_agent_mcp()
    exit(0 if result else 1)
