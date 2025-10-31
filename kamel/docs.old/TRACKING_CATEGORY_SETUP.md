# TRACKING CATEGORY SETUP - VALUATION ADJUSTMENTS

**Purpose**: Track all P&L normalization adjustments for buyer valuation
**Category Name**: Valuation Adjustments
**Status**: REQUIRED BEFORE STAGE 2 JOURNAL CREATION

---

## TRACKING CATEGORY STRUCTURE

### Category Name
```
Valuation Adjustments
```

### Category Options (3 Total)

**Option 1: Normalized Operations**
- **Name**: Normalized Operations
- **Purpose**: Core business adjustments and operating normalizations
- **Usage**: Future operating expense adjustments, one-off expense removals

**Option 2: Owner Personal**
- **Name**: Owner Personal
- **Purpose**: Personal expenses excluded from business operations
- **Usage**: Stage 1 journal entries (personal wages, rent, insurance, etc.)
- **Amount**: R1,415,856 (Stage 1)

**Option 3: Owner Property**
- **Name**: Owner Property
- **Purpose**: Income/expenses from owner's property not in sale
- **Usage**: Stage 2 journal entries (rental income from 11 Ypsilanti Ave)
- **Amount**: R1,512,000 (Stage 2)

---

## XERO CREATION METHODS

### Method 1: Via Xero Web Interface

**Steps:**
1. Navigate to **Settings** → **General Settings** → **Tracking Categories**
2. Click **Add Tracking Category**
3. Enter category details:
   - **Name**: Valuation Adjustments
   - **Description**: P&L normalization adjustments for business valuation
4. Click **Save**
5. Add options:
   - Click **Add Option**
   - Option 1: "Normalized Operations"
   - Option 2: "Owner Personal"
   - Option 3: "Owner Property"
6. Click **Save** after each option
7. Verify all three options are visible

**Screenshot reference locations:**
- Settings (gear icon, top right)
- General Settings → Tracking Categories
- List should show new category with 3 options

### Method 2: Via Xero API

**Create Tracking Category:**
```json
POST https://api.xero.com/api.xro/2.0/TrackingCategories

{
  "Name": "Valuation Adjustments",
  "Options": [
    {
      "Name": "Normalized Operations"
    },
    {
      "Name": "Owner Personal"
    },
    {
      "Name": "Owner Property"
    }
  ]
}
```

**Headers:**
```
Authorization: Bearer {access_token}
xero-tenant-id: {tenant_id}
Content-Type: application/json
Accept: application/json
```

**Expected Response:**
```json
{
  "TrackingCategories": [
    {
      "TrackingCategoryID": "xxxxx-xxxxx-xxxxx-xxxxx",
      "Name": "Valuation Adjustments",
      "Status": "ACTIVE",
      "Options": [
        {
          "TrackingOptionID": "yyyyy-yyyyy-yyyyy-yyyyy",
          "Name": "Normalized Operations",
          "Status": "ACTIVE"
        },
        {
          "TrackingOptionID": "zzzzz-zzzzz-zzzzz-zzzzz",
          "Name": "Owner Personal",
          "Status": "ACTIVE"
        },
        {
          "TrackingOptionID": "aaaaa-aaaaa-aaaaa-aaaaa",
          "Name": "Owner Property",
          "Status": "ACTIVE"
        }
      ]
    }
  ]
}
```

**Important**: Record the `TrackingCategoryID` for use in journal entries.

---

## USAGE GUIDELINES

### When to Use Each Option

**Normalized Operations:**
- Non-recurring expenses to remove
- One-time capital expenditures to adjust
- Abnormal operating costs
- Future-state normalization adjustments

**Owner Personal:**
- Stage 1 adjustments (COMPLETED)
- Personal wages paid through business
- Personal insurance, rent, interest
- Personal vehicle expenses
- Owner personal expenses of any kind

**Owner Property:**
- Stage 2 adjustments (IN PROGRESS)
- Rental income from 11 Ypsilanti Ave
- Property expenses for 11 Ypsilanti Ave (if any)
- Any owner real estate not in sale

### Reporting Benefits

**P&L Reports:**
- Filter by tracking category to see normalized vs. actual
- Show only "Valuation Adjustments" to see all normalizations
- Exclude tracking category to see buyer's operating P&L

**Audit Trail:**
- Clear documentation of all adjustments
- Traceable back to normalization stages
- Easy to reverse or modify if needed

**Buyer Communication:**
- Professional presentation of adjustments
- Clear categorization for due diligence
- Transparent normalization methodology

---

## VALIDATION CHECKLIST

**After Creation:**
- [ ] Category name is exactly "Valuation Adjustments"
- [ ] All 3 options are created
- [ ] Option names match exactly:
  - [ ] "Normalized Operations"
  - [ ] "Owner Personal"
  - [ ] "Owner Property"
- [ ] Category status is ACTIVE
- [ ] All options status is ACTIVE
- [ ] Category appears in tracking category list
- [ ] Category ID recorded: ________________

**Before Using in Journals:**
- [ ] Test tracking category selection in a test transaction
- [ ] Verify options appear in dropdown
- [ ] Confirm tracking appears in transaction reports
- [ ] Test P&L filtering by tracking category

---

## INTEGRATION WITH MANUAL JOURNALS

### Stage 1 Journal (Personal Expenses)
**When created, apply tracking:**
```
Tracking Category: Valuation Adjustments
Option: Owner Personal
Transactions: All lines of Stage 1 journal
Amount: R1,415,856
```

### Stage 2 Journal (Rental Income)
**Apply tracking:**
```
Tracking Category: Valuation Adjustments
Option: Owner Property
Transactions: All lines of Stage 2 journal
Amount: R1,512,000
```

### Future Normalizations
**Use Normalized Operations for:**
- Abnormal expenses to remove
- One-time capital expenditures
- Non-recurring operating costs
- Any other normalization adjustments

---

## REPORTING EXAMPLES

### View All Normalization Adjustments
```
Report: Profit & Loss
Date Range: 01 Feb 2024 - 31 Jan 2025
Tracking Category: Valuation Adjustments
Options: ALL

Result: Shows all adjusted transactions totaling R2,927,856
```

### View Normalized Operating P&L
```
Report: Profit & Loss
Date Range: 01 Feb 2024 - 31 Jan 2025
Tracking Category: Valuation Adjustments
Filter: EXCLUDE tracking category

Result: Shows buyer's normalized operating business only
```

### View by Adjustment Type
```
Report: Profit & Loss
Date Range: 01 Feb 2024 - 31 Jan 2025
Tracking Category: Valuation Adjustments
Option: Owner Personal

Result: Shows R1,415,856 in personal expense adjustments
```

---

## TROUBLESHOOTING

**Issue**: Can't create tracking category
- **Solution**: Check Xero permissions (need Advisor or Standard user role)

**Issue**: Options not appearing in dropdown
- **Solution**: Refresh Xero interface, or log out and back in

**Issue**: Tracking category not showing in reports
- **Solution**: Ensure transactions have tracking applied, check report filters

**Issue**: API returns error
- **Solution**: Check bearer token validity, verify tenant ID

**Issue**: Duplicate category name error
- **Solution**: Category may already exist, check existing categories first

---

## ALTERNATIVE APPROACH

If tracking categories can't be created, use **Class** or **Department** features instead:
- Navigate to Settings → Class/Department
- Create same structure
- Apply to journal entries similarly

**Note**: Tracking categories are preferred for clarity and reporting flexibility.

---

## NEXT STEPS

1. Create tracking category using preferred method
2. Record tracking category ID
3. Verify all 3 options are active
4. Apply "Owner Personal" to Stage 1 journal (if not already done)
5. Apply "Owner Property" to Stage 2 journal
6. Test P&L report filtering
7. Proceed with journal creation

---

**Document Created**: 2025-01-21
**Priority**: CRITICAL - Required before Stage 2 journal creation
**Estimated Time**: 5 minutes via web interface
