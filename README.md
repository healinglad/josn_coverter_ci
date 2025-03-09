# GitLeaks Report Converter

A versatile tool for scanning repositories for secrets and converting GitLeaks reports to Excel format. This repository provides two ways to use the tool:

1. **Web Interface**: A modern Flask-based web application with drag-and-drop functionality
2. **GitHub Actions Workflow**: Automated CI workflow for scanning repositories

## Features

- 🔍 Scan repositories for various types of secrets:
  - API Keys and Tokens
  - Private Keys (RSA, SSH)
  - AWS Access Tokens
  - Stripe API Keys
  - OAuth Client Secrets
  - And more...
- 📊 Convert GitLeaks JSON reports to organized Excel format
- 🎨 Modern web interface with Tailwind CSS
- 🔄 GitHub Actions workflow for automated scanning
- 📋 Detailed Excel reports including:
  - File location and line numbers
  - Secret type and description
  - Rule ID and detection details
  - Commit information
  - Author and date

## Web Interface Usage

1. **Setup**:
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Start the Flask server
   python app.py
   ```

2. **Using the Web Interface**:
   - Open your browser and navigate to `http://localhost:5000`
   - Drag and drop your GitLeaks JSON report or click to upload
   - Click "Convert" to generate the Excel report
   - Download the converted Excel file

### Web Interface Screenshots

#### Main Upload Page
![Main Upload Interface](docs/images/upload_interface.png)
*Modern drag-and-drop interface for uploading GitLeaks JSON reports*

#### File Processing
![File Processing](docs/images/processing.png)
*Real-time feedback during report conversion*

#### Download Page
![Download Report](docs/images/download.png)
*Download page showing the converted Excel report*

## GitHub Actions Workflow Usage

1. **Setup**:
   - Copy the `.github/workflows/scan_repository.yml` to your repository
   - Ensure you have the necessary permissions set up

2. **Running the Workflow**:
   - Go to your repository's Actions tab
   - Select "GitLeaks Scanner"
   - Click "Run workflow"
   - Enter the repository URL to scan
   - Wait for the workflow to complete
   - Download the Excel report from the workflow artifacts

### GitHub Actions Screenshots

#### Workflow Selection
![Workflow Selection](docs/images/workflow_select.png)
*Selecting the GitLeaks Scanner workflow*

#### Running the Workflow
![Run Workflow](docs/images/workflow_run.png)
*Initiating a new scan with repository URL*

#### Workflow Results
![Workflow Results](docs/images/workflow_results.png)
*Viewing scan results and downloading the Excel report*

## Excel Report Format

The generated Excel report includes:
- File: Location of the secret
- Line: Line number in the file
- Secret Type: Description of the secret type
- Rule ID: GitLeaks rule that detected the secret
- Secret: The detected secret value
- Commit: First 8 characters of the commit hash
- Author: Commit author
- Email: Author's email
- Date: Commit date

### Excel Report Screenshot
![Excel Report](docs/images/excel_report.png)
*Sample Excel report showing detected secrets with formatting*

## Dependencies

- Python 3.x
- Flask
- Pandas
- OpenPyXL
- GitLeaks (for scanning)
- Additional requirements in `requirements.txt`

## Security Note

This tool is designed for security testing and auditing purposes. Never commit real secrets to version control, and always follow security best practices when handling sensitive information.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.

## License

MIT License - See LICENSE file for details
