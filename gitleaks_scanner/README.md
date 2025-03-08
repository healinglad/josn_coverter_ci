# GitLeaks Scanner Module

A standalone module for scanning repositories using GitLeaks and generating Excel reports. This module is part of the GitLeaks Report Converter project but can be used independently through GitHub Actions.

## Features
- Scan any GitHub repository using GitLeaks
- Automatically convert findings to Excel format
- Download reports as workflow artifacts
- Easy integration with CI/CD pipelines

## Usage

The GitHub Actions workflow is available at the root level of the project (`.github/workflows/scan_repository.yml`). To use it:

1. Go to your repository's "Actions" tab
2. Select "GitLeaks Scanner" workflow
3. Click "Run workflow"
4. Enter the GitHub repository URL to scan
5. Download the Excel report from workflow artifacts when complete

## Directory Structure
```
project_root/
├── .github/
│   └── workflows/
│       └── scan_repository.yml    # Main workflow file
└── gitleaks_scanner/
    ├── scripts/
    │   └── report_converter.py    # JSON to Excel converter
    └── README.md                  # Module documentation
```

## Report Format
The generated Excel report includes:
- File path
- Line number
- Commit hash
- Secret found
- Rule ID
- Date
- Author
- Email

## Development
The `report_converter.py` script can be used independently to convert GitLeaks JSON reports to Excel format. To use it directly:

1. Place your GitLeaks JSON report as `gitleaks-report.json` in the same directory
2. Run: `python report_converter.py`
3. Find the generated Excel file in the `excel_outputs` directory
