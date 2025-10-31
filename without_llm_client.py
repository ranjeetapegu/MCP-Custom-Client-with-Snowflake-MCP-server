"""
Simple MCP Client - NO LLM Required
Direct calls to Snowflake MCP server
"""

import asyncio
import httpx
import os
import json
from dotenv import load_dotenv

load_dotenv()

class SimpleMCPClient:
    """MCP Client without LLM - Direct tool calls"""
    
    def __init__(self):
        # Configuration from .env
        self.account = os.getenv('SNOWFLAKE_ACCOUNT')
        self.database = os.getenv('SNOWFLAKE_DATABASE')
        self.schema = os.getenv('SNOWFLAKE_SCHEMA')
        self.server = os.getenv('SNOWFLAKE_MCP_SERVER')
        self.token = os.getenv('SNOWFLAKE_PAT_TOKEN')
        
        # Build endpoint
        self.base_url = (
            f"https://{self.account}.snowflakecomputing.com"
            f"/api/v2/databases/{self.database}/schemas/{self.schema}"
            f"/mcp-servers/{self.server}"
        )
        
        # Headers
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
    
    async def call_mcp(self, method: str, params: dict = None):
        """Direct MCP call - no LLM"""
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params or {}
        }
        
        async with httpx.AsyncClient(verify=False, timeout=30.0) as client:
            response = await client.post(
                self.base_url,
                json=payload,
                headers=self.headers
            )
            return response.json()
    
    async def initialize(self):
        """Initialize MCP server"""
        result = await self.call_mcp(
            "initialize",
            {"protocolVersion": "2024-11-05"}
        )
        return result
    
    async def list_tools(self):
        """Get available tools"""
        result = await self.call_mcp("tools/list")
        return result.get('result', {}).get('tools', [])
    
    async def search_movies(self, query: str, limit: int = 10):
        """Search movies - direct call, no LLM"""
        result = await self.call_mcp(
            "tools/call",
            {
                "name": "moviemaster-search",
                "arguments": {
                    "query": query,
                    "limit": limit
                }
            }
        )
        return result
    
    async def search_actors(self, query: str, limit: int = 10):
        """Search actors - direct call, no LLM"""
        result = await self.call_mcp(
            "tools/call",
            {
                "name": "moviemaster-actor-search",
                "arguments": {
                    "query": query,
                    "limit": limit
                }
            }
        )
        return result
    
    async def analyze(self, message: str):
        """Semantic analysis - direct call, no LLM"""
        result = await self.call_mcp(
            "tools/call",
            {
                "name": "imdb-semantic-view",
                "arguments": {
                    "message": message
                }
            }
        )
        return result


async def main():
    """Example usage - No LLM needed!"""
    
    client = SimpleMCPClient()
    
    print("🎬 Simple MCP Client (No LLM)")
    print("=" * 60)
    
    # Initialize
    print("\n1. Initializing...")
    init_result = await client.initialize()
    print(f"✅ Connected to MCP server")
    
    # List tools
    print("\n2. Available tools:")
    tools = await client.list_tools()
    for tool in tools:
        print(f"   - {tool['name']}")
    
    # Direct movie search - NO LLM!
    print("\n3. Searching for Tom Hanks movies...")
    movies = await client.search_movies("Tom Hanks", limit=5)
    print(json.dumps(movies, indent=2))
    
    # Direct actor search - NO LLM!
    print("\n4. Searching for actors...")
    actors = await client.search_actors("Oscar winning", limit=3)
    print(json.dumps(actors, indent=2))
    
    # Direct analytics - NO LLM!
    print("\n5. Running analytics...")
    analysis = await client.analyze("Show top 5 movies by rating")
    print(json.dumps(analysis, indent=2))

if __name__ == "__main__":
    asyncio.run(main())