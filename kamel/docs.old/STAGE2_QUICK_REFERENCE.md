# STAGE 2 QUICK REFERENCE - Rental Income Exclusion

**At-a-Glance Summary for Fast Execution**

---

## 🎯 OBJECTIVE
Remove R1,512,000 rental income from buyer's P&L (owner's property not in sale)

---

## 💰 KEY NUMBERS
| Item | Amount | Account |
|------|--------|---------|
| Monthly Rental | R126,000 | 201 |
| Annual Rental | R1,512,000 | 201 |
| Reclassify To | R1,512,000 | 881 |
| Property | 11 Ypsilanti Ave | N/A |
| Sale Status | NOT INCLUDED | N/A |

---

## 📝 MANUAL JOURNAL ENTRY

**Quick Copy-Paste:**
```
Date: 2025-01-31
Reference: MJ-STAGE2-RENTAL-EXCLUSION
Narration: Rental income exclusion - owner property (11 Ypsilanti Ave) not included in business sale

Line 1:
  DR  201  Rental Income                R1,512,000.00
  Tracking: Valuation Adjustments / Owner Property

Line 2:
  CR  881  Owner A Funds Introduced     R1,512,000.00
  Tracking: Valuation Adjustments / Owner Property

Status: DRAFT
```

---

## 🏷️ TRACKING CATEGORY

**Name:** Valuation Adjustments

**Options:**
1. Normalized Operations
2. Owner Personal ← Stage 1
3. Owner Property ← Stage 2 (USE THIS)

---

## 📊 P&L IMPACT

**Before:**
- Revenue: R3,512,000 (includes R1.5M rental)

**After:**
- Revenue: R2,000,000 (operating only)
- Rental Income: R0 ✅

---

## ✅ VALIDATION CHECKLIST

**Before Creating:**
- [ ] Tracking category exists
- [ ] Amount = R1,512,000 exactly
- [ ] Accounts 201 & 881 exist

**After Creating:**
- [ ] Journal ID recorded: ________
- [ ] Debits = Credits
- [ ] Status = DRAFT
- [ ] Tracking applied both lines

**Before Posting:**
- [ ] P&L shows R0 rental income
- [ ] User approval obtained
- [ ] Stage 1 journal also ready

---

## 📂 SUPPORTING DOCS

1. `MANUAL_JOURNAL_STAGE2_SPEC.md` - Full specifications
2. `TRACKING_CATEGORY_SETUP.md` - Category setup
3. `NORMALIZED_PL_REPORT_INSTRUCTIONS.md` - Report guide
4. `HANDOVER_STAGE2_TO_STAGE3.md` - Complete handover

---

## ⚡ FASTEST EXECUTION PATH

**Web Interface (5 steps):**
1. Accounting → Advanced → Manual Journals → New
2. Date: 31/01/2025, Ref: MJ-STAGE2-RENTAL-EXCLUSION
3. Line 1: DR 201, R1,512,000, Tracking: Owner Property
4. Line 2: CR 881, R1,512,000, Tracking: Owner Property
5. Save as DRAFT → Record ID

**Done!** ✅

---

## 🚨 COMMON ERRORS

**"Tracking category not found"**
→ Create category first (see TRACKING_CATEGORY_SETUP.md)

**"Journal doesn't balance"**
→ Both lines must be R1,512,000 exactly

**"Account code invalid"**
→ Verify 201 and 881 exist in chart of accounts

**"Can't save as DRAFT"**
→ Check Xero permissions (need Advisor role)

---

## 🎯 NEXT STEPS

1. Create journal (DRAFT)
2. Record journal ID
3. Generate draft P&L
4. Verify rental income = R0
5. Get user approval
6. Post journal (DRAFT → POSTED)
7. Generate final P&L

---

## 📞 STAGE 3 HANDOVER

**Once Stage 2 complete, execute:**
```
STAGE 3: Final Validation & Posting
- Review both journals (Stages 1 & 2)
- Post both journals
- Generate final normalized P&L
- Create valuation package
```

**Start here:** `HANDOVER_STAGE2_TO_STAGE3.md`

---

**END OF QUICK REFERENCE**
*Full details in supporting documentation*
