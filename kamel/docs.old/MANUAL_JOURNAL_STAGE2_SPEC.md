# MANUAL JOURNAL ENTRY - STAGE 2: RENTAL INCOME RECLASSIFICATION

**Date**: 2025-01-31
**Status**: READY FOR XERO CREATION
**Purpose**: Exclude rental income from buyer's normalized P&L (owner property not in sale)

---

## JOURNAL ENTRY DETAILS

### Header Information
```
Journal Type: MANUAL
Journal Date: 2025-01-31
Reference: MJ-STAGE2-RENTAL-EXCLUSION
Narration: Rental income exclusion - owner property (11 Ypsilanti Ave) not included in business sale
Status: DRAFT (to be posted after validation)
```

### Line Items

**Line 1 - Debit Rental Income:**
```
Account Code: 201
Account Name: Rental Income
Description: Rental income - 11 Ypsilanti Ave (owner property not in sale)
Debit Amount: R1,512,000.00
Credit Amount: R0.00
Tax Type: No Tax
Tracking Category: Valuation Adjustments / Owner Property
```

**Line 2 - Credit Owner Funds Introduced:**
```
Account Code: 881
Account Name: Owner A Funds Introduced
Description: Reclassify rental income - owner property not included in sale
Debit Amount: R0.00
Credit Amount: R1,512,000.00
Tax Type: No Tax
Tracking Category: Valuation Adjustments / Owner Property
```

### Journal Totals
- **Total Debits**: R1,512,000.00
- **Total Credits**: R1,512,000.00
- **Difference**: R0.00 ✅ (balanced)

---

## XERO CREATION METHODS

### Method 1: Via Xero Web Interface (Manual Entry)

**Steps:**
1. Navigate to Accounting → Advanced → Manual Journals
2. Click "New Manual Journal"
3. Enter header details:
   - Date: 31/01/2025
   - Reference: MJ-STAGE2-RENTAL-EXCLUSION
   - Narration: "Rental income exclusion - owner property (11 Ypsilanti Ave) not included in business sale"
4. Add Line 1:
   - Account: 201 (Rental Income)
   - Description: "Rental income - 11 Ypsilanti Ave (owner property not in sale)"
   - Debit: 1512000.00
   - Tracking: Valuation Adjustments > Owner Property
5. Add Line 2:
   - Account: 881 (Owner A Funds Introduced)
   - Description: "Reclassify rental income - owner property not included in sale"
   - Credit: 1512000.00
   - Tracking: Valuation Adjustments > Owner Property
6. Verify totals balance
7. Save as DRAFT
8. Record Journal ID for handover

### Method 2: Via Xero API (Automated)

**JSON Payload:**
```json
{
  "Type": "MANUAL",
  "Date": "2025-01-31",
  "LineAmountTypes": "NoTax",
  "Status": "DRAFT",
  "Reference": "MJ-STAGE2-RENTAL-EXCLUSION",
  "Narration": "Rental income exclusion - owner property (11 Ypsilanti Ave) not included in business sale",
  "JournalLines": [
    {
      "LineAmount": 1512000.00,
      "AccountCode": "201",
      "Description": "Rental income - 11 Ypsilanti Ave (owner property not in sale)",
      "TrackingCategories": [
        {
          "Name": "Valuation Adjustments",
          "Option": "Owner Property"
        }
      ]
    },
    {
      "LineAmount": -1512000.00,
      "AccountCode": "881",
      "Description": "Reclassify rental income - owner property not included in sale",
      "TrackingCategories": [
        {
          "Name": "Valuation Adjustments",
          "Option": "Owner Property"
        }
      ]
    }
  ]
}
```

**API Endpoint:**
```
POST https://api.xero.com/api.xro/2.0/ManualJournals
Headers:
  Authorization: Bearer {access_token}
  xero-tenant-id: {tenant_id}
  Content-Type: application/json
  Accept: application/json
```

### Method 3: Via CData SQL Insert (If Available)

```sql
-- Note: Check if CData supports INSERT into ManualJournals table
-- This is for reference only, verify capability first

INSERT INTO [Xero-KPC].ACCOUNTING.ManualJournals (
  Type,
  Date,
  Status,
  Reference,
  Narration,
  LineAmount1,
  AccountCode1,
  Description1,
  LineAmount2,
  AccountCode2,
  Description2
)
VALUES (
  'MANUAL',
  '2025-01-31',
  'DRAFT',
  'MJ-STAGE2-RENTAL-EXCLUSION',
  'Rental income exclusion - owner property (11 Ypsilanti Ave) not included in business sale',
  1512000.00,
  '201',
  'Rental income - 11 Ypsilanti Ave (owner property not in sale)',
  -1512000.00,
  '881',
  'Reclassify rental income - owner property not included in sale'
);
```

---

## VALIDATION CHECKLIST

**Before Posting:**
- [ ] Journal balances (debits = credits)
- [ ] Tracking category exists and is applied
- [ ] Account codes are correct (201, 881)
- [ ] Date is end of financial period (31 Jan 2025)
- [ ] Narration clearly explains purpose
- [ ] Amount matches annual rental income (R1,512,000)
- [ ] Status is DRAFT (not posted yet)

**After Creation:**
- [ ] Record Journal ID: ________________
- [ ] Verify appears in Manual Journals list
- [ ] Confirm tracking category visible
- [ ] Save Journal ID to STAGE 3 handover

**Before Final Posting:**
- [ ] Review with Stage 1 journal (personal expenses)
- [ ] Generate draft P&L to verify impact
- [ ] Confirm both journals ready together
- [ ] Get user approval if required

---

## EXPECTED P&L IMPACT

### Before Journal Entry:
```
Revenue
├── Sales (wholesale pottery)        R2,000,000
├── Rental Income (Account 201)      R1,512,000
└── Total Revenue                    R3,512,000
```

### After Journal Entry:
```
Revenue
├── Sales (wholesale pottery)        R2,000,000
├── Rental Income (Account 201)      R0 ← ADJUSTED
└── Total Revenue                    R2,000,000 ← NORMALIZED

Equity
└── Owner A Funds Introduced (881)   +R1,512,000 ← RECLASSIFIED
```

**Effect**: Removes rental income from P&L, moves to equity section as owner contribution.

---

## INTEGRATION WITH STAGE 1

**Combined Normalization Effect:**

| Adjustment | Stage | Amount | Account | Impact |
|------------|-------|--------|---------|--------|
| Personal expenses | 1 | R1,415,856 | 880 (Drawings) | Remove from OpEx |
| Rental income | 2 | R1,512,000 | 881 (Introduced) | Remove from Revenue |
| **Net Effect** | Combined | **-R2,927,856** | **P&L normalized** | **Operating business only** |

---

## TROUBLESHOOTING

**Issue**: Tracking category doesn't exist
- **Solution**: Create tracking category first (see TRACKING_CATEGORY_SETUP.md)

**Issue**: Account codes not found
- **Solution**: Verify chart of accounts, may need to create accounts 880, 881

**Issue**: Journal won't balance
- **Solution**: Check line amounts are exactly equal (debits = credits)

**Issue**: Can't save as DRAFT
- **Solution**: Xero permissions issue, may need admin access

**Issue**: Xero MCP server not connected
- **Solution**: Use manual web interface method OR reconnect MCP server

---

## NEXT STEPS AFTER CREATION

1. Record Journal ID in handover document
2. Generate normalized P&L report (DRAFT state is fine)
3. Verify rental income shows as R0
4. Verify total revenue reflects operating business only
5. Proceed to STAGE 3 validation and posting

---

**Document Created**: 2025-01-21
**Ready for Execution**: YES ✅
**Dependencies**: Tracking category must exist (create first if needed)
