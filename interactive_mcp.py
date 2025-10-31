import asyncio
import json
from without_llm_client import SimpleMCPClient

async def interactive():
    client = SimpleMCPClient()
    
    # Initialize
    await client.initialize()
    print("✅ Connected to IMDB MCP Server (No LLM)")
    
    while True:
        print("\n" + "="*60)
        print("Options:")
        print("  1. Search Movies")
        print("  2. Search Actors")
        print("  3. Run Analytics")
        print("  4. Exit")
        print("="*60)
        
        choice = input("\nSelect (1-4): ").strip()
        
        if choice == '1':
            query = input("Movie search query: ")
            result = await client.search_movies(query, limit=5)
            print("\n📊 Results:")
            print(json.dumps(result, indent=2))
        
        elif choice == '2':
            query = input("Actor search query: ")
            result = await client.search_actors(query, limit=5)
            print("\n📊 Results:")
            print(json.dumps(result, indent=2))
        
        elif choice == '3':
            message = input("Analytics query: ")
            result = await client.analyze(message)
            print("\n📊 Results:")
            print(json.dumps(result, indent=2))
        
        elif choice == '4':
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    asyncio.run(interactive())