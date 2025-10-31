"""
Report generator for bank reconciliation discrepancies
"""
import pandas as pd
import json
from datetime import datetime
from typing import List, Dict, Any
import io

class ReportGenerator:
    """Generate reports for reconciliation discrepancies"""
    
    def __init__(self):
        pass
    
    def generate_summary_report(self, discrepancies: List[Dict[str, Any]]) -> str:
        """
        Generate a summary report of discrepancies
        
        Args:
            discrepancies (List[Dict[str, Any]]): List of discrepancies
            
        Returns:
            str: Summary report text
        """
        if not discrepancies:
            return "No discrepancies found. Bank statement and Xero data are fully reconciled."
        
        # Count discrepancy types
        type_counts = {}
        for disc in discrepancies:
            disc_type = disc['type']
            type_counts[disc_type] = type_counts.get(disc_type, 0) + 1
        
        # Calculate total discrepancy amount
        total_unmatched_bank = sum(d['amount'] for d in discrepancies if d['type'] == 'unmatched_bank')
        total_unmatched_xero = sum(d['amount'] for d in discrepancies if d['type'] == 'unmatched_xero')
        
        report = f"""
BANK RECONCILIATION DISCREPANCY REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

SUMMARY
=======
Total Discrepancies: {len(discrepancies)}

DISCREPANCY TYPES
=================
"""
        for disc_type, count in type_counts.items():
            report += f"{disc_type.replace('_', ' ').title()}: {count}\n"
        
        report += f"""
FINANCIAL IMPACT
================
Unmatched Bank Entries: R{total_unmatched_bank:,.2f}
Unmatched Xero Entries: R{total_unmatched_xero:,.2f}
Net Difference: R{total_unmatched_bank + total_unmatched_xero:,.2f}

RECOMMENDATIONS
===============
1. Review unmatched bank entries to determine if they should be recorded in Xero
2. Review unmatched Xero entries to determine if they have corresponding bank transactions
3. Investigate duplicate entries and remove/merge as appropriate
4. Ensure all transactions have proper references and descriptions
"""
        
        return report.strip()
    
    def generate_detailed_csv(self, discrepancies: List[Dict[str, Any]]) -> str:
        """
        Generate detailed CSV report of discrepancies
        
        Args:
            discrepancies (List[Dict[str, Any]]): List of discrepancies
            
        Returns:
            str: CSV formatted report
        """
        if not discrepancies:
            return "No discrepancies found."
        
        # Convert to DataFrame
        df = pd.DataFrame(discrepancies)
        
        # Format date column
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
        
        # Convert to CSV
        output = io.StringIO()
        df.to_csv(output, index=False)
        return output.getvalue()
    
    def generate_action_plan(self, discrepancies: List[Dict[str, Any]]) -> str:
        """
        Generate action plan for resolving discrepancies
        
        Args:
            discrepancies (List[Dict[str, Any]]): List of discrepancies
            
        Returns:
            str: Action plan text
        """
        if not discrepancies:
            return "No action required. All transactions are reconciled."
        
        action_plan = f"""
BANK RECONCILIATION ACTION PLAN
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

IMMEDIATE ACTIONS
=================
"""
        
        # Group discrepancies by type
        grouped = {}
        for disc in discrepancies:
            disc_type = disc['type']
            if disc_type not in grouped:
                grouped[disc_type] = []
            grouped[disc_type].append(disc)
        
        # Add actions for each type
        for disc_type, discs in grouped.items():
            action_plan += f"\n{disc_type.replace('_', ' ').upper()} ENTRIES ({len(discs)} items)\n"
            action_plan += "-" * (len(disc_type) + 15) + "\n"
            
            for i, disc in enumerate(discs[:10], 1):  # Limit to first 10 for brevity
                action_plan += f"{i}. Date: {disc['date'].strftime('%Y-%m-%d') if hasattr(disc['date'], 'strftime') else disc['date']}, "
                action_plan += f"Amount: R{disc['amount']:,.2f}, "
                action_plan += f"Description: {disc.get('description', 'N/A')}\n"
                action_plan += f"   Action: {disc['details']}\n\n"
            
            if len(discs) > 10:
                action_plan += f"   ... and {len(discs) - 10} more entries\n\n"
        
        action_plan += """
NEXT STEPS
==========
1. Assign responsibility for each discrepancy to team members
2. Set deadlines for resolution of each discrepancy type
3. Schedule follow-up review in 1 week
4. Update Xero records with any missing transactions
5. Verify bank statement accuracy with financial institution if needed

DOCUMENTATION
=============
- Keep all correspondence related to discrepancy resolution
- Note reasons for any adjustments made
- Maintain audit trail of all changes
"""
        
        return action_plan.strip()
    
    def get_recommendations(self, discrepancies: List[Dict[str, Any]]) -> List[str]:
        """
        Get recommendations for handling discrepancies
        
        Args:
            discrepancies (List[Dict[str, Any]]): List of discrepancies
            
        Returns:
            List[str]: List of recommendations
        """
        if not discrepancies:
            return ["No discrepancies found. Reconciliation is complete."]
        
        recommendations = []
        
        # Count types
        type_counts = {}
        for disc in discrepancies:
            disc_type = disc['type']
            type_counts[disc_type] = type_counts.get(disc_type, 0) + 1
        
        # Generate recommendations based on types found
        if type_counts.get('unmatched_bank', 0) > 0:
            recommendations.append(f"Review {type_counts['unmatched_bank']} bank entries not found in Xero - these may need to be recorded in the accounting system")
        
        if type_counts.get('unmatched_xero', 0) > 0:
            recommendations.append(f"Review {type_counts['unmatched_xero']} Xero entries not found in bank statements - verify if these transactions actually occurred")
        
        if type_counts.get('duplicate_bank', 0) > 0:
            recommendations.append(f"Check {type_counts['duplicate_bank']} potential duplicate bank entries - remove or merge as appropriate")
        
        if type_counts.get('duplicate_xero', 0) > 0:
            recommendations.append(f"Check {type_counts['duplicate_xero']} potential duplicate Xero entries - remove or merge as appropriate")
        
        recommendations.append("Ensure all future transactions include detailed references for easier reconciliation")
        recommendations.append("Consider implementing automated reconciliation tools for regular monitoring")
        
        return recommendations