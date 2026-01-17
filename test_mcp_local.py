"""
Test KaggleRun MCP Server Locally

This script tests the MCP tools without needing a full MCP client.
You need a valid KAGGLE_JUPYTER_URL to test with a real Kaggle kernel.

Usage:
    # Set your Kaggle URL first
    set KAGGLE_JUPYTER_URL=https://your-kaggle-url/proxy

    # Run this test
    python test_mcp_local.py
"""

import os
import sys
import asyncio

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from kagglerun.mcp_server import TOOLS, handle_tool_call


def print_tools():
    """Print all available MCP tools."""
    print("=" * 60)
    print("KAGGLERUN MCP TOOLS")
    print("=" * 60)

    for tool in TOOLS:
        print(f"\n[{tool['name']}]")
        print(f"  Description: {tool['description'][:80]}...")

        schema = tool['inputSchema']
        props = schema.get('properties', {})
        required = schema.get('required', [])

        if props:
            print("  Parameters:")
            for name, details in props.items():
                req = "(required)" if name in required else "(optional)"
                print(f"    - {name}: {details.get('type', 'any')} {req}")

    print("\n" + "=" * 60)


async def test_tool(name: str, arguments: dict):
    """Test a single MCP tool."""
    print(f"\n>>> Testing tool: {name}")
    print(f"    Arguments: {arguments}")
    print("-" * 40)

    result = await handle_tool_call(name, arguments)
    print(result)
    print("-" * 40)
    return result


async def main():
    # Print available tools
    print_tools()

    # Check if URL is set
    url = os.environ.get('KAGGLE_JUPYTER_URL')
    if not url:
        print("\n[WARNING] KAGGLE_JUPYTER_URL not set!")
        print("Set it to test with a real Kaggle kernel:")
        print("  Windows: set KAGGLE_JUPYTER_URL=https://your-url/proxy")
        print("  Linux:   export KAGGLE_JUPYTER_URL=https://your-url/proxy")
        print("\nRunning mock tests only...\n")
        return

    print(f"\n[INFO] Using URL: {url[:50]}...")

    # Test connection
    await test_tool("test_connection", {})

    # Test get GPU info
    await test_tool("get_gpu_info", {})

    # Test get system info
    await test_tool("get_system_info", {})

    # Test execute Python
    await test_tool("execute_python", {
        "code": "print('Hello from KaggleRun MCP!')\nimport sys; print(f'Python: {sys.version}')"
    })

    # Test list files
    await test_tool("list_files", {"path": "/kaggle/working/"})

    # Test save file
    await test_tool("save_file", {
        "filename": "mcp_test.txt",
        "content": "This file was created by KaggleRun MCP test!"
    })

    # Test read file
    await test_tool("read_file", {"path": "mcp_test.txt"})

    print("\n" + "=" * 60)
    print("MCP TESTS COMPLETE!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
