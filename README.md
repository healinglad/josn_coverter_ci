# GitLeaks Report Converter

A web application that converts GitLeaks JSON reports into Excel files for easier tracking and management of security findings.

## Features

- Upload GitLeaks JSON reports via drag-and-drop or file browser
- Automatic conversion to Excel format
- Download generated Excel files
- Modern, responsive web interface
- Tracks key information: File, Line, Commit, Secret, RuleID, Date, and Author

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Drag and drop your GitLeaks JSON report or click "Browse Files" to select it
2. The file will be automatically converted to Excel format
3. Download the generated Excel file from the list below
4. All generated Excel files are stored in the `excel_outputs` directory

## Directory Structure

- `uploads/`: Temporary storage for uploaded JSON files
- `excel_outputs/`: Storage for generated Excel files
- `templates/`: HTML templates
- `app.py`: Main Flask application
- `requirements.txt`: Python dependencies
