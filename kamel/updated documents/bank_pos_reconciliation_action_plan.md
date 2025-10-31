# Bank to POS Reconciliation - Action Plan

## Current Status of Payment Matching

### ✅ Completed Matches

#### Major Customers Identified
| Customer | Bank Reference | 2024 Total | 2025 YTD | Payment Method |
|----------|---------------|------------|-----------|----------------|
| African Paper Products | "African Paper Produc" | R180,000 | R178,777 | EFT/Settlement |
| Vegmore Distribution | Cards/Various | R295,409 | R177,950 | Mixed |
| Egg Designs | "Egg Designs" | R435,199 | R48,999 | EFT/Settlement |
| Kamel Kilns | "Kamel" references | Various | R27,620 | Internal transfer |

#### Recurring Card Payments Identified
- **Card ending 2676**: Astron Energy, Genashle, Durban locations
- **Card ending 2702**: Multiple transactions, appears to be main business card
- **Card ending 2759**: External/Brolink transactions

### 🔄 In Progress - Need Resolution

#### Unmatched Bank Deposits (Examples from Feb 2024)
| Date | Amount | Reference | Likely Match |
|------|--------|-----------|--------------|
| 23/02/2024 | R1,500.00 | Digital Payment Cr | ? |
| 23/02/2024 | R1,000.00 | Digital Payment Dt | ? |
| 26/02/2024 | R23,786.73 | Digital Payment Dt | Large customer? |
| 26/02/2024 | R20,000.00 | Digital Payment Dt | Possibly African Paper |
| 26/02/2024 | R6,000.00 | Digital Payment Dt | ? |

#### Mystery Payments Needing Investigation
1. **ACB Credit entries** - Appear regularly, varying amounts
2. **Spar River/La Lucia B** - R2,000-4,000 recurring
3. **Vodacom references** - Multiple small payments
4. **Settlement entries** - Generic, need specific customer links

## Recommended Reconciliation Process

### Step 1: Data Preparation (Day 1-2)

1. **Export all bank statements to Excel**
   - Columns: Date, Description, Reference, Debit, Credit, Balance
   - Clean data: Remove duplicates, fix formatting

2. **Export POS sales data**
   - Daily sales summaries
   - Individual transaction logs if available
   - Payment method breakdowns

3. **Create matching template**
   ```
   Date | Bank Amount | Bank Ref | POS Amount | Customer | Status | Notes
   ```

### Step 2: Automated Matching (Day 3-4)

**Python Script Framework:**
```python
# Key matching rules to implement:
1. Exact amount match within 2-day window
2. Reference text pattern matching (fuzzy logic)
3. Card number last 4 digits extraction
4. Regular customer pattern recognition
5. Round amount identification (likely invoice payments)
```

### Step 3: Manual Review Process (Day 5-7)

#### Priority Matches to Confirm
1. **All payments over R10,000** - Major customers
2. **Recurring monthly amounts** - Contract customers
3. **Round numbers** (R20,000, R5,000) - Invoice settlements
4. **Card clusters** - Same card, multiple daily transactions

#### Investigation Required
- Contact customers for payment confirmations
- Cross-reference with invoice numbers
- Check delivery records for timing matches

## Customer Identification Enhancement

### Immediate Actions

1. **Create Customer Database**
   ```
   Customer ID | Name | Card Numbers | Bank Ref | Avg Transaction | Frequency
   ```

2. **Pattern Recognition Rules**
   - Egg Designs: Look for "Egg" in reference
   - African Paper: "African", "Paper", round R20,000 amounts
   - Vegmore: Multiple small transactions, cards 2676/2702
   - Digital payments: Match amounts to invoices

3. **Missing Customer Investigation**
   - Art Culture Alliance - Last payment date?
   - Mathnwu Pottery - Contact details?
   - Roti and Chai - Payment pattern?

## Technology Implementation Plan

### Week 1: Quick Wins
1. **Excel Macro for Basic Matching**
   - VLOOKUP for exact amounts
   - Text search for customer names
   - Date range matching

2. **Bank Statement Parser**
   - PDF to CSV converter
   - Standardize formats
   - Clean reference fields

### Week 2: Advanced Matching
1. **Database Setup**
   - Customer master table
   - Transaction history table
   - Payment method mapping

2. **Matching Algorithm**
   - Implement fuzzy matching
   - Machine learning for patterns
   - Confidence scoring system

### Week 3: Reporting System
1. **Dashboard Creation**
   - Matched vs unmatched percentages
   - Customer payment trends
   - Outstanding reconciliation items

2. **Alert System**
   - Large unmatched deposits
   - Missing regular payments
   - Unusual transaction patterns

## Specific Tasks for Allen Van Houten

### This Week
☐ Request from Diana:
- Complete invoice listing for 2024-2025
- Customer contact database
- Any manual payment records/notes
- Explanation for major unmatched deposits

☐ Analysis to complete:
- Calculate match rate for September 2025
- Identify top 10 unmatched deposits
- List all recurring payment patterns

### Next Week
☐ Customer outreach:
- Call Egg Designs about payment status
- Confirm African Paper Products payment schedule
- Verify Vegmore Distribution payment methods

☐ System setup:
- Install reconciliation software
- Create customer ID mapping table
- Set up automated matching rules

### Before Deal Closure
☐ Complete reconciliation:
- 100% of 2024 payments matched
- 95%+ of 2025 YTD matched
- All customers identified and verified

☐ Documentation:
- Customer payment history report
- Aged receivables analysis
- Payment method breakdown

## Risk Flags to Monitor

⚠️ **High Priority Concerns:**
1. Multiple R20,000 payments - verify all are from African Paper
2. Large February deposit (R23,786) - identify customer
3. Declining card transaction volumes in 2025
4. No clear Art Culture Alliance payments in 2025

🔍 **Investigation Required:**
1. Why are Egg Designs payments dropping?
2. Are Vegmore payments being made regularly?
3. Any bounced payments or reversals?
4. Customer credit terms being extended?

## Success Metrics

### Reconciliation Targets
- **Week 1:** 70% of transactions matched
- **Week 2:** 85% matched, all major customers identified
- **Week 3:** 95% matched, system automated
- **Month end:** 100% reconciled, dashboard operational

### Customer Identification Goals
- Identify 100% of customers over R10,000 annual spend
- Map 90% of card payments to specific customers
- Create profiles for top 20 customers
- Document payment patterns for all regular customers

---

*Action Plan Created: October 4, 2025*  
*Priority: Bank-to-POS Reconciliation*  
*Timeline: 3-4 weeks to full implementation*  
*Critical Path: Customer identification for due diligence*