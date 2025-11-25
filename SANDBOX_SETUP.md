# Web Voice Agent Sandbox Setup Guide

## Quick Start

### 1. Create the Sandbox
Go to: https://cloud.livekit.io/
- Navigate to **Sandbox** section
- Click **"Create sandbox"** button
- Select template: **agent-starter-react**
- Name (optional): `oyatalk-sandbox`
- Enable capabilities:
  - ✓ Audio
  - ✓ Camera (optional)
  - ✓ Chat
  - ✓ Audio buffer (recommended - speeds up connection)
- Click **Create**

### 2. You'll Get a URL Like
```
https://oyatalk-sandbox-XXXXXX.sandbox.livekit.io
```

### 3. Share & Test
- Open the URL in any browser
- Click "Join" or "Start Conversation"
- Speak or type to your agent

---

## Testing MCP Integration

### Test Questions
Ask your agent these questions to verify MCP is working:

1. **"Tell me about the LiveKit turn detector"**
   - Should mention searching documentation
   - Will provide specific technical details

2. **"How do I use MCP servers with LiveKit agents?"**
   - Should reference current docs
   - Will explain the architecture

3. **"What are the latest LiveKit features?"**
   - Should pull from live documentation
   - Not just general knowledge

4. **"How do I register MCP tools with an agent?"**
   - Specific question about your current setup
   - Will search docs for accurate answer

### How to Verify MCP is Working
✅ **Success signs:**
- Agent mentions "searching documentation" or "looking this up"
- Specific quotes from LiveKit docs
- Recent/current information
- Exact technical details

❌ **Failure signs:**
- Generic/training-data answers
- No mention of tools being used
- Outdated information
- Vague responses

---

## Current Agent Configuration

**Agent ID:** `A_jt99atS8EyaJ`  
**Status:** Ready (Self-hosted)  
**MCP Servers:** 5 configured
- LiveKit Docs (active)
- Filesystem (requires local server)
- Git (requires local server)
- SQLite (requires local server)
- Time (requires local server)

**Model Stack:**
- STT: AssemblyAI Universal Streaming
- LLM: OpenAI GPT-4.1 Mini
- TTS: Cartesia Sonic-3
- Turn Detection: Multilingual Model

---

## Troubleshooting

### Agent doesn't respond?
- Check agent status in LiveKit dashboard
- Verify worker is "Ready"
- Check agent logs for errors

### MCP not working?
- Verify LiveKit Docs server is accessible
- Check browser console for errors
- Try a different LiveKit-specific question

### Audio/connection issues?
- Enable "Audio buffer" in sandbox settings
- Check browser permissions for microphone
- Try a different browser

---

## Next Steps

After testing:
1. ✅ Verify MCP integration works
2. ✅ Test various conversation flows
3. ✅ Deploy to production with `lk agent create`
4. ✅ Add custom tools as needed
5. ✅ Scale up worker count if needed
