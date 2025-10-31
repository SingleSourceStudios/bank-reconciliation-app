# Claude Code MCP Server Configuration

This folder contains the MCP (Model Context Protocol) server configuration for this project.

## Xero MCP Server

The Xero MCP server is configured to provide integration with Xero accounting APIs.

### Configuration

The server is configured in `claude_desktop_config.json` with the following settings:

- **Server**: `@xeroapi/xero-mcp-server@latest`
- **Client ID**: `C27722EE62294491B96F6DB84FAC0D4C`
- **Client Secret**: Configured (stored securely)

### Usage

To use the Xero MCP server in Claude Code:

1. Ensure you have the latest version of Claude Code installed
2. The server will automatically start when Claude Code loads this project
3. You can access Xero functionality through MCP tool calls

### Available Tools

The Xero MCP server provides tools for:
- Organization management
- Invoice operations
- Contact management
- Account queries
- And more Xero API functionality

For full documentation, visit: https://github.com/XeroAPI/xero-mcp-server

### Troubleshooting

If the server doesn't load:
1. Verify Node.js and npm are installed
2. Check that the credentials are correct
3. Restart Claude Code
4. Check Claude Code logs for error messages

### Security Note

⚠️ **Important**: The credentials in this configuration should be kept secure. Do not commit this configuration to public repositories.
