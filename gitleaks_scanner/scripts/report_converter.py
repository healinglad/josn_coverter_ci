import pandas as pd
import json
from datetime import datetime
import os

EXCEL_FOLDER = 'excel_outputs'
os.makedirs(EXCEL_FOLDER, exist_ok=True)

def parse_gitleaks_report(file_path):
    """
    Parse GitLeaks text-based report format into a structured format.
    
    Args:
        file_path (str): Path to the GitLeaks report file
        
    Returns:
        list: List of findings with extracted information
    """
    findings = []
    current_finding = {}
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if not line:
            if current_finding:
                findings.append(current_finding)
                current_finding = {}
            continue
            
        if ':' in line:
            key, value = [x.strip() for x in line.split(':', 1)]
            if key == 'Finding':
                if current_finding:
                    findings.append(current_finding)
                current_finding = {}
            current_finding[key] = value
            
    if current_finding:
        findings.append(current_finding)
    
    return findings

def convert_json_to_excel(json_file_path):
    """
    Convert GitLeaks JSON report to Excel format with proper formatting.
    
    Args:
        json_file_path (str): Path to the GitLeaks JSON report file
        
    Returns:
        str: Path to the generated Excel file
    """
    try:
        # Parse the gitleaks report format
        data = parse_gitleaks_report(json_file_path)
        
        # Extract relevant fields
        processed_data = []
        for finding in data:
            processed_data.append({
                'File': finding.get('File', ''),
                'Line': finding.get('Line', ''),
                'Commit': finding.get('Commit', ''),
                'Secret': finding.get('Secret', ''),
                'RuleID': finding.get('RuleID', ''),
                'Date': finding.get('Date', ''),
                'Author': finding.get('Author', ''),
                'Email': finding.get('Email', '')
            })
        
        df = pd.DataFrame(processed_data)
        
        # Generate unique filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        excel_path = os.path.join(EXCEL_FOLDER, f'gitleaks_report_{timestamp}.xlsx')
        
        # Save to Excel with auto-adjusted column widths
        with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Findings')
            worksheet = writer.sheets['Findings']
            
            # Auto-adjust column widths
            for idx, col in enumerate(df.columns):
                max_length = max(
                    df[col].astype(str).apply(len).max(),
                    len(col)
                ) + 2
                worksheet.column_dimensions[chr(65 + idx)].width = min(max_length, 50)
            
            # Add basic formatting
            header_row = worksheet[1]
            for cell in header_row:
                cell.font = cell.font.copy(bold=True)
                cell.fill = cell.fill.copy(
                    patternType='solid',
                    fgColor='E0E0E0'
                )
        
        print(f"Successfully created Excel report: {excel_path}")
        return excel_path
    
    except Exception as e:
        print(f"Error converting file: {str(e)}")
        raise

if __name__ == '__main__':
    input_file = 'gitleaks-report.json'
    if os.path.exists(input_file):
        try:
            excel_path = convert_json_to_excel(input_file)
            print(f"Successfully converted report to: {excel_path}")
        except Exception as e:
            print(f"Failed to convert report: {str(e)}")
            exit(1)
    else:
        print(f"Error: {input_file} not found")
        exit(1)
