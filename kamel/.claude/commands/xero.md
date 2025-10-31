---
command: "/xero"
category: "Integration & API"
purpose: "Interact with Xero accounting API for financial data management"
wave-enabled: false
performance-profile: "standard"
---

# Xero Accounting Integration

Access Xero accounting data and perform financial operations through the Xero MCP server.

## Available Operations

### Contacts Management
- List contacts
- Get contact details
- Search contacts by name or criteria

### Reports & Analytics
- View financial reports
- Access profit/loss statements
- Generate balance sheets
- Custom report queries

### Transactions
- View invoices
- Track payments
- Manage bills
- Process receipts

### Settings & Configuration
- Access account settings
- View organization details
- Manage payment terms

## Usage Examples

**List all contacts:**
```
Can you fetch all contacts from Xero?
```

**Get financial reports:**
```
Show me the profit and loss statement for last quarter
```

**Search invoices:**
```
Find all unpaid invoices from the last 30 days
```

**Contact details:**
```
Get details for contact "ABC Company"
```

## Auto-Activation

This command auto-activates when:
- Keywords: "xero", "invoice", "accounting", "financial report", "contact"
- Tasks involving: financial data, accounting operations, business reports

## Personas

- **Primary**: Backend Developer (API integration)
- **Secondary**: Analyzer (financial data analysis)

## MCP Tools Used

All Xero operations use the `mcp__xero__*` tool family:
- Contact management tools
- Report generation tools
- Transaction query tools
- Settings access tools

## Security Notes

⚠️ **Important**: Bearer tokens expire regularly. Update your token in:
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

For production use, consider implementing:
1. OAuth2 authentication flow
2. Automatic token refresh
3. Environment variable storage
4. Token encryption

## Rate Limits

Xero API has rate limits:
- 60 requests per minute (standard apps)
- 5,000 requests per day (per organization)

Plan bulk operations accordingly.

## Scopes Available

Current token scopes:
- `accounting.contacts.read` - Read contact information
- `accounting.settings.read` - Read organization settings
- `accounting.reports.read` - Access financial reports
- `accounting.transactions` - Full transaction access
- `offline_access` - Refresh token capability

## Troubleshooting

**Token expired error:**
1. Log into Xero Developer Portal
2. Generate new bearer token
3. Update Claude Code MCP config
4. Restart Claude Code

**Permission denied:**
- Check token scopes match required operation
- Verify organization access permissions

**Rate limit exceeded:**
- Implement request batching
- Add delay between operations
- Use bulk endpoints when available
