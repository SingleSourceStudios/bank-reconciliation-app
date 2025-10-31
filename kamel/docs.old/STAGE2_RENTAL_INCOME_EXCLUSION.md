# STAGE 2: RENTAL INCOME RECLASSIFICATION
**Date**: 2025-01-21
**Status**: IN PROGRESS
**Objective**: Exclude rental income from normalized P&L (owner's property not included in sale)

## CONTEXT FROM STAGE 1 ✅
- Manual Journal ID: `e6b7038c-c568-4256-8515-7b0d3029dd5b`
- Personal expenses reclassified: R117,988/month → Owner's Drawings (880)
- Status: DRAFT (ready to post)

## RENTAL INCOME DETAILS

### Property Information
- **Address**: 11 Ypsilanti Avenue (owner's personal rental property)
- **Sale Status**: NOT INCLUDED in Kamel Potteries sale
- **Impact**: Rental income must be excluded from buyer's normalized P&L

### Financial Data
- **Monthly Rental Income**: R126,000
- **Annual Rental Income**: R1,512,000 (12 months)
- **Account Code**: 201 (Rental Income)
- **Percentage of Total Revenue**: ~47% (very material!)

### Rationale
The rental income of R1,512,000 per annum represents 47% of reported revenue but:
1. Property (11 Ypsilanti Ave) is owner's personal asset
2. NOT part of Kamel Potteries business sale
3. Buyer will NOT receive this income stream
4. Must be excluded from valuation P&L

## MANUAL JOURNAL ENTRY REQUIRED

### Journal Details
```
Date: 2025-01-31
Reference: MJ-STAGE2-RENTAL
Narration: "Rental income exclusion - owner property (11 Ypsilanti Ave) not included in business sale"

Line Items:
DR  201  Rental Income                 R1,512,000.00
CR  881  Owner A Funds Introduced      R1,512,000.00
```

### Effect on P&L
**Before Normalization:**
- Sales: ~R2,000,000
- Rental Income: R1,512,000
- Total Revenue: ~R3,512,000

**After Stage 2 Normalization:**
- Sales: ~R2,000,000
- Rental Income: R0 (reclassified to Owner Introduced)
- Total Revenue: ~R2,000,000 (business operations only)

## TRACKING CATEGORY SETUP

Create tracking category for all normalization adjustments:

**Category Name**: "Valuation Adjustments"
**Options**:
1. "Normalized Operations" - Core business adjustments
2. "Owner Personal" - Personal expense reclassifications
3. "Owner Property" - Rental income from owner's property

Apply "Owner Property" tracking to this journal entry.

## NEXT STEPS FOR STAGE 2

### Sub-Phase 2A: Data Verification ⏳
- [x] Confirm rental income monthly amount: R126,000
- [x] Calculate annual total: R1,512,000
- [ ] Verify Xero account code 201 contains only rental income
- [ ] Check for any other non-operating income

### Sub-Phase 2B: Manual Journal Creation ⏳
- [ ] Create manual journal with above details
- [ ] Apply "Owner Property" tracking category
- [ ] Set status to DRAFT
- [ ] Record journal ID for handover

### Sub-Phase 2C: Validation ⏳
- [ ] Generate normalized P&L report
- [ ] Verify rental income = R0
- [ ] Confirm total revenue reflects operating income only
- [ ] Document normalized revenue figures

## CRITICAL ACCOUNT CODES REFERENCE

| Code | Account Name | Purpose |
|------|--------------|---------|
| 201  | Rental Income | Source of rental income (to be zeroed) |
| 880  | Owner A Drawings | Personal expenses destination |
| 881  | Owner A Funds Introduced | Rental income destination |
| 477  | Wages | Operating expense |
| 433  | Insurance | Operating expense |
| 469  | Rent | Operating expense |
| 437  | Interest | Operating expense |
| 429  | General Expenses | Operating expense |

## COMPLETION CRITERIA

Stage 2 complete when:
- [x] Rental income total verified: R1,512,000/year
- [ ] Manual journal created and saved as DRAFT
- [ ] Journal ID documented for handover
- [ ] Tracking category created and applied
- [ ] Normalized P&L shows R0 rental income
- [ ] Handover document created for STAGE 3
- [ ] All working documents saved to `/docs` folder

## XERO MCP SERVER STATUS
⚠️ **Current Issue**: Xero MCP server not currently connected to Claude Code
**Workaround**: Document journal entry specifications for manual creation or next session

### Manual Journal Entry Format for Xero
```json
{
  "Type": "MANUAL",
  "Date": "2025-01-31",
  "LineAmountTypes": "NoTax",
  "Status": "DRAFT",
  "Narration": "Rental income exclusion - owner property (11 Ypsilanti Ave) not included in business sale",
  "JournalLines": [
    {
      "AccountCode": "201",
      "Description": "Rental income - 11 Ypsilanti Ave (owner property)",
      "LineAmount": 1512000.00,
      "TrackingCategories": [
        {
          "Name": "Valuation Adjustments",
          "Option": "Owner Property"
        }
      ]
    },
    {
      "AccountCode": "881",
      "Description": "Rental income - owner property not in sale",
      "LineAmount": -1512000.00,
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

## HANDOVER TO STAGE 3

Once Stage 2 complete, next chat should execute:

**STAGE 3: FINAL NORMALIZATION & VALIDATION**
1. Review both manual journals (Stage 1 + Stage 2)
2. Post both journals from DRAFT → POSTED
3. Generate final normalized P&L report
4. Create valuation summary document
5. Document normalized EBITDA calculation

---

**Document Created**: 2025-01-21
**Last Updated**: {{timestamp}}
**Next Action**: Complete Sub-Phase 2B (Manual Journal Creation)
