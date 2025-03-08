from flask import Flask, render_template, request, send_file, jsonify
import pandas as pd
import json
from datetime import datetime
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
EXCEL_FOLDER = 'excel_outputs'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(EXCEL_FOLDER, exist_ok=True)

def parse_gitleaks_report(file_path):
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
            for idx, col in enumerate(df.columns):
                max_length = max(
                    df[col].astype(str).apply(len).max(),
                    len(col)
                ) + 2
                worksheet.column_dimensions[chr(65 + idx)].width = min(max_length, 50)
        
        return excel_path
    except Exception as e:
        print(f"Error converting file: {str(e)}")
        raise

@app.route('/')
def index():
    excel_files = [f for f in os.listdir(EXCEL_FOLDER) if f.endswith('.xlsx')]
    return render_template('index.html', excel_files=excel_files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not file.filename.endswith('.json'):
        return jsonify({'error': 'Only JSON files are allowed'}), 400
    
    try:
        # Save uploaded file
        json_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(json_path)
        
        # Convert to Excel
        excel_path = convert_json_to_excel(json_path)
        excel_filename = os.path.basename(excel_path)
        
        # Clean up the uploaded JSON file
        os.remove(json_path)
        
        return jsonify({
            'success': True,
            'message': 'File converted successfully',
            'excel_file': excel_filename
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(
        os.path.join(EXCEL_FOLDER, filename),
        as_attachment=True,
        download_name=filename
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
