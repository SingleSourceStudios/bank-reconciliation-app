# Xero Integration Guide

Complete guide for integrating and using Xero accounting API through Claude Code.

## Overview

The Xero MCP server provides seamless integration with Xero's accounting platform, enabling automated financial operations, report generation, and data management.

## Setup

### Prerequisites
- Xero account with API access
- Xero Developer Portal access
- Valid bearer token with required scopes

### Configuration

The Xero MCP server is already configured in Claude Code. Configuration location:
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

Current configuration:
```json
{
  "xero": {
    "command": "npx",
    "args": ["-y", "@xeroapi/xero-mcp-server@latest"],
    "env": {
      "XERO_CLIENT_BEARER_TOKEN": "<your-token>"
    }
  }
}
```

### Security Best Practices

⚠️ **Never commit bearer tokens to version control**

**Recommended approach:**

1. **Use environment variables** (`.env` file):
```bash
XERO_CLIENT_BEARER_TOKEN=your-token-here
```

2. **Update Claude Code config** to reference env var:
```json
{
  "xero": {
    "command": "npx",
    "args": ["-y", "@xeroapi/xero-mcp-server@latest"],
    "env": {
      "XERO_CLIENT_BEARER_TOKEN": "${XERO_CLIENT_BEARER_TOKEN}"
    }
  }
}
```

3. **Add to `.gitignore`**:
```
.env
.env.local
```

## Token Management

### Getting a Bearer Token

1. **Xero Developer Portal**:
   - Visit https://developer.xero.com/
   - Navigate to "My Apps"
   - Select your app or create new one
   - Go to "Configuration" → "OAuth 2.0 credentials"

2. **Generate Token**:
   - Use OAuth2 flow for production
   - Bearer tokens from portal expire after 30 minutes
   - Implement token refresh for long-running operations

### Token Scopes

Available scopes for accounting integration:
- `accounting.contacts.read` - Read contact information
- `accounting.contacts` - Full contact management
- `accounting.settings.read` - Organization settings
- `accounting.reports.read` - Financial reports
- `accounting.transactions` - Transaction operations
- `accounting.transactions.read` - Read-only transactions
- `offline_access` - Refresh token capability

### Token Expiration

**Current token expires**: Check JWT payload `exp` field
- Standard bearer tokens: 30 minutes
- Refresh tokens: 60 days

**Auto-refresh implementation** (recommended for production):
```javascript
// Example token refresh logic
const refreshToken = async () => {
  const response = await fetch('https://identity.xero.com/connect/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      grant_type: 'refresh_token',
      refresh_token: process.env.XERO_REFRESH_TOKEN,
      client_id: process.env.XERO_CLIENT_ID,
      client_secret: process.env.XERO_CLIENT_SECRET
    })
  });
  return response.json();
};
```

## Usage Patterns

### Basic Operations

**List contacts:**
```
/xero list all contacts
```

**Get specific contact:**
```
/xero get contact details for "ABC Corporation"
```

**Financial reports:**
```
/xero show profit and loss for Q4 2024
```

**Invoice management:**
```
/xero find unpaid invoices older than 30 days
```

### Advanced Queries

**Custom report with filters:**
```
/xero generate balance sheet as of December 31, 2024
```

**Bulk operations:**
```
/xero export all contacts to CSV format
```

**Transaction analysis:**
```
/xero analyze spending patterns by category for last quarter
```

## API Rate Limits

**Xero API Limits:**
- **Per minute**: 60 requests
- **Per day**: 5,000 requests per organization
- **Concurrent**: 5 simultaneous requests

**Best practices:**
- Batch requests when possible
- Cache frequently accessed data
- Implement exponential backoff on rate limit errors
- Use webhooks for real-time updates instead of polling

**Rate limit headers:**
```
X-Rate-Limit-Problem: minute
X-Rate-Limit-Retry-After: 60
```

## Error Handling

### Common Errors

**401 Unauthorized**:
- Token expired or invalid
- Solution: Generate new bearer token

**403 Forbidden**:
- Insufficient scopes
- Solution: Request additional OAuth scopes

**429 Too Many Requests**:
- Rate limit exceeded
- Solution: Implement backoff and retry logic

**500 Internal Server Error**:
- Xero service issue
- Solution: Check Xero status page, retry later

### Debugging Tips

1. **Check MCP server logs**:
```bash
# Claude Code console (Help → Toggle Developer Tools)
# Look for xero-mcp-server output
```

2. **Validate token**:
```bash
# Decode JWT to check expiration
# Visit https://jwt.io/ and paste token
```

3. **Test connection**:
```
/xero test connection and list available organizations
```

## Integration Examples

### Financial Dashboard

```
/xero create a financial summary dashboard showing:
- Current bank balance
- Accounts receivable aging
- Top 5 expenses this month
- Revenue vs. budget comparison
```

### Automated Reporting

```
/xero generate monthly financial package including:
- Profit & Loss statement
- Balance Sheet
- Cash Flow projection
- Top 10 customers by revenue
```

### Contact Management

```
/xero sync contacts and:
- Identify duplicates
- Update contact categories
- Flag inactive customers (no transactions in 90 days)
```

## Troubleshooting

### MCP Server Not Responding

1. **Restart Claude Code**
2. **Check MCP server installation**:
```bash
npx -y @xeroapi/xero-mcp-server@latest --version
```

3. **Verify configuration**:
```bash
cat "$HOME/Library/Application Support/Claude/claude_desktop_config.json" | jq '.mcpServers.xero'
```

### Token Issues

**Token expired**:
1. Generate new token from Xero Developer Portal
2. Update configuration
3. Restart Claude Code

**Invalid scopes**:
1. Check required scopes for operation
2. Request additional scopes in Xero app settings
3. Regenerate token with new scopes

### Performance Issues

**Slow responses**:
- Reduce query complexity
- Filter data at API level
- Use pagination for large datasets

**Timeout errors**:
- Increase timeout in MCP config
- Break large operations into smaller chunks

## Production Deployment

### OAuth2 Flow Implementation

For production applications, implement full OAuth2 flow:

1. **Authorization Code Flow**:
   - Redirect users to Xero authorization URL
   - Exchange auth code for access token
   - Store refresh token securely

2. **Token Storage**:
   - Use encrypted database or secrets manager
   - Never store tokens in plain text
   - Implement token rotation

3. **Webhook Integration**:
   - Subscribe to Xero webhooks for real-time updates
   - Reduce API polling
   - Improve data freshness

### Monitoring

**Track metrics**:
- API request count and rate
- Token refresh frequency
- Error rates by type
- Response times

**Alerting**:
- Token expiration warnings
- Rate limit approaching threshold
- Service degradation

## Resources

- **Xero Developer Portal**: https://developer.xero.com/
- **API Documentation**: https://developer.xero.com/documentation/
- **OAuth2 Guide**: https://developer.xero.com/documentation/guides/oauth2/overview/
- **MCP Server**: https://www.npmjs.com/package/@xeroapi/xero-mcp-server
- **Support**: https://developer.xero.com/support/

## Next Steps

1. ✅ Xero MCP server configured
2. ✅ Slash command `/xero` available
3. 🔄 Implement OAuth2 for production
4. 🔄 Set up token refresh automation
5. 🔄 Configure webhooks for real-time updates
6. 🔄 Build custom financial dashboards

---

**Security Reminder**: Rotate your bearer token regularly and never commit tokens to version control.
