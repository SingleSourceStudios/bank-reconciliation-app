# NORMALIZED P&L REPORT - GENERATION INSTRUCTIONS

**Purpose**: Generate normalized Profit & Loss showing buyer's operating business only
**Date Range**: 01 February 2024 - 31 January 2025 (12-month period)
**Status**: READY TO EXECUTE (after Stage 1 & 2 journals created)

---

## REPORT SPECIFICATIONS

### Report Type
```
Profit & Loss Statement
(aka Income Statement)
```

### Date Range
```
From: 01 February 2024
To: 31 January 2025
Period: 12 months
```

### Comparison Options
```
No comparison (single period only)
OR
Compare to: Actual P&L (before normalization)
```

### Layout
```
Standard layout
Cash or Accrual: Accrual basis
Tracking Categories: ALL (show breakdown)
```

---

## GENERATION METHODS

### Method 1: Via Xero Web Interface

**Steps:**
1. Navigate to **Accounting** → **Reports**
2. Find and click **Profit and Loss**
3. Set date range:
   - From: 01/02/2024
   - To: 31/01/2025
4. Click **Update**
5. Customize report (click **Settings** gear icon):
   - Show Tracking Categories: YES
   - Layout: Standard
   - Basis: Accrual
6. Click **Update**
7. Review report structure
8. Export options:
   - **PDF**: Professional presentation
   - **Excel**: Detailed analysis
   - **CSV**: Data manipulation

### Method 2: Via Xero API

**Endpoint:**
```
GET https://api.xero.com/api.xro/2.0/Reports/ProfitAndLoss

Query Parameters:
?fromDate=2024-02-01
&toDate=2025-01-31
&standardLayout=true
&paymentsOnly=false
```

**Headers:**
```
Authorization: Bearer {access_token}
xero-tenant-id: {tenant_id}
Accept: application/json
```

### Method 3: Via CData SQL Query

```sql
-- Get P&L summary data
SELECT
  Account_Type,
  Account_Name,
  Account_Code,
  SUM(Total) as Amount,
  COUNT(*) as Transaction_Count
FROM [Xero-KPC].ACCOUNTING.BankTransactions
WHERE Date >= '2024-02-01'
  AND Date <= '2025-01-31'
GROUP BY Account_Type, Account_Name, Account_Code
ORDER BY Account_Type, Account_Name;
```

**Note**: This gives raw data; manual P&L construction needed.

---

## EXPECTED REPORT STRUCTURE

### Revenue Section (NORMALIZED)

```
Revenue
├── Sales - Wholesale Pottery          R2,000,000
├── Rental Income (Account 201)        R0         ← ADJUSTED via Stage 2
└── Total Revenue                      R2,000,000
```

### Cost of Goods Sold (if tracked)
```
Cost of Goods Sold
├── Materials                          Rxxxxx
├── Direct Labor                       Rxxxxx
└── Total COGS                         Rxxxxx
```

### Gross Profit
```
Gross Profit = Revenue - COGS
```

### Operating Expenses (NORMALIZED)

**Before Stage 1 Adjustments:**
```
Operating Expenses
├── Wages (477)                        R1,200,000  (includes personal)
├── Insurance (433)                    R120,000    (includes personal)
├── Rent (469)                         R60,000     (includes personal)
├── Interest (437)                     R24,000     (includes personal)
├── General Expenses (429)             R12,000     (includes personal)
└── Other operating expenses           Rxxxxx
```

**After Stage 1 Adjustments:**
```
Operating Expenses
├── Wages (477)                        R200,000    ← NORMALIZED
├── Insurance (433)                    R0          ← NORMALIZED
├── Rent (469)                         R0          ← NORMALIZED
├── Interest (437)                     R0          ← NORMALIZED
├── General Expenses (429)             R0          ← NORMALIZED
├── Other operating expenses           Rxxxxx
└── Total Operating Expenses           R~400,000   ← NORMALIZED
```

### Net Profit (NORMALIZED)
```
Net Profit = Gross Profit - Operating Expenses
```

---

## VERIFICATION CHECKLIST

### Before Report Generation:
- [ ] Stage 1 journal created (personal expenses)
- [ ] Stage 2 journal created (rental income)
- [ ] Both journals saved as DRAFT
- [ ] Tracking categories applied
- [ ] Date range correct (01 Feb 2024 - 31 Jan 2025)

### During Report Review:
- [ ] Rental Income (201) shows R0
- [ ] Personal wages removed from Wages (477)
- [ ] Personal insurance removed from Insurance (433)
- [ ] Personal rent removed from Rent (469)
- [ ] Personal interest removed from Interest (437)
- [ ] Personal expenses removed from General (429)
- [ ] Total revenue is ~R2,000,000 (operating only)
- [ ] Operating expenses reduced by ~R1,415,856

### Expected Key Metrics:

| Metric | Before Normalization | After Normalization | Change |
|--------|---------------------|---------------------|--------|
| Total Revenue | R3,512,000 | R2,000,000 | -R1,512,000 (rental) |
| Operating Expenses | R1,815,856 | R400,000 | -R1,415,856 (personal) |
| Net Profit | R~1,696,144 | R~1,600,000 | -R~96,144 |
| EBITDA | Calculate | Calculate | Compare |

---

## COMPARISON REPORT (RECOMMENDED)

### Side-by-Side Comparison

**Column 1: Actual (Before Normalization)**
- Shows all transactions as recorded
- Includes personal expenses
- Includes rental income
- Total revenue: R3,512,000

**Column 2: Normalized (After Adjustments)**
- Excludes personal expenses (Stage 1)
- Excludes rental income (Stage 2)
- Operating business only
- Total revenue: R2,000,000

**Column 3: Adjustments**
- Shows difference between columns
- Highlights normalization impact
- Clear audit trail

**How to Create:**
1. Generate report twice:
   - Once with tracking categories EXCLUDED (normalized)
   - Once with ALL data (actual)
2. Export both to Excel
3. Create side-by-side comparison
4. Add variance column

---

## EXPORT FORMATS

### PDF Export
**Use for:**
- Buyer presentations
- Professional documentation
- Email attachments
- Printed reports

**Settings:**
- Include report header
- Show company logo
- Show tracking categories
- Portrait orientation

### Excel Export
**Use for:**
- Detailed analysis
- Custom calculations
- EBITDA computation
- Valuation models

**Includes:**
- All line items
- Formulas preserved
- Tracking data
- Formatting maintained

### CSV Export
**Use for:**
- Data integration
- Custom reporting tools
- Further processing
- Database import

**Format:**
- Comma-separated values
- Header row included
- Raw numbers (no formatting)

---

## POST-GENERATION ANALYSIS

### Calculate Normalized EBITDA

**Formula:**
```
EBITDA = Net Profit + Interest + Taxes + Depreciation + Amortization

Where:
- Net Profit = From normalized P&L
- Interest = Interest expense (if any remaining)
- Taxes = Tax expense
- Depreciation = From asset register
- Amortization = From intangible assets
```

### Key Ratios to Calculate

**Profitability:**
- Gross Profit Margin = (Gross Profit / Revenue) × 100
- Net Profit Margin = (Net Profit / Revenue) × 100
- EBITDA Margin = (EBITDA / Revenue) × 100

**Efficiency:**
- Operating Expense Ratio = (OpEx / Revenue) × 100
- Labor Cost % = (Wages / Revenue) × 100

**Valuation Metrics:**
- Price-to-Sales Multiple
- EBITDA Multiple
- Profit Multiple

---

## TROUBLESHOOTING

**Issue**: Report still shows rental income
- **Solution**: Verify Stage 2 journal is created and DRAFT status
- **Solution**: Check journal date is within report period
- **Solution**: Regenerate report after journal creation

**Issue**: Personal expenses still showing
- **Solution**: Verify Stage 1 journal is created
- **Solution**: Check all account codes are correct
- **Solution**: Verify tracking categories applied

**Issue**: Numbers don't match expectations
- **Solution**: Check date range is exactly 01 Feb 2024 - 31 Jan 2025
- **Solution**: Verify basis is Accrual (not Cash)
- **Solution**: Check for any unreconciled transactions

**Issue**: Can't export report
- **Solution**: Check Xero permissions
- **Solution**: Try different export format
- **Solution**: Clear browser cache

---

## NEXT STEPS AFTER REPORT GENERATION

1. **Review Report Quality**
   - Verify all normalizations applied correctly
   - Check calculations are accurate
   - Confirm format is professional

2. **Create Supporting Documentation**
   - Schedule of adjustments (Stages 1 & 2)
   - Explanation of normalization methodology
   - Backup calculations for key metrics

3. **Prepare Buyer Presentation Package**
   - Normalized P&L (PDF)
   - Adjustment schedule (Excel)
   - EBITDA calculation (Excel)
   - Executive summary (Word/PDF)

4. **Proceed to STAGE 3**
   - Final validation of all journals
   - Post journals from DRAFT to POSTED
   - Generate final reports
   - Create valuation summary

---

## SAMPLE REPORT INTERPRETATION

**For Buyer:**

> "The normalized P&L shows Kamel Potteries' **operating business only**, with two key adjustments:
>
> 1. **Personal Expenses Removed** (R1,415,856/year):
>    - Owner's personal wages, insurance, rent, and other personal costs
>    - These expenses will not transfer to the buyer
>    - Improves operating margin significantly
>
> 2. **Rental Income Excluded** (R1,512,000/year):
>    - Income from owner's personal property (11 Ypsilanti Ave)
>    - Property is NOT included in the business sale
>    - Buyer will not receive this income stream
>
> **Result**: The normalized P&L reflects the **true operating performance** of the pottery manufacturing and wholesale business that the buyer is acquiring, showing approximately **R2,000,000 in annual operating revenue** with normalized operating expenses of **~R400,000**, resulting in strong operating margins."

---

**Document Created**: 2025-01-21
**Ready to Execute**: After Stage 1 & 2 journals created
**Estimated Time**: 15 minutes (generation + review)
