#!/usr/bin/env python3
"""
VGGT-MPS: MCP Server for 3D Vision on Apple Silicon
Provides tools for 3D reconstruction using VGGT model with MPS acceleration
"""

from fastmcp import FastMCP
from vggt_mps.tools.readme import readme_mcp
from vggt_mps.tools.demo_gradio import demo_gradio_mcp
from vggt_mps.tools.demo_viser import demo_viser_mcp
from vggt_mps.tools.demo_colmap import demo_colmap_mcp

# Create MCP server for VGGT-MPS
mcp = FastMCP(name="vggt-mps")

# Mount tool servers
mcp.mount(readme_mcp)
mcp.mount(demo_gradio_mcp)
mcp.mount(demo_viser_mcp)
mcp.mount(demo_colmap_mcp)

if __name__ == "__main__":
    mcp.run()

def main():
    """Entry point for MCP server"""
    mcp.run()