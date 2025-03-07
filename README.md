# Document Automation Tasks

This repository contains Python scripts designed for automating various document-related tasks. The functionalities include:
- Formatting document data
- Auto-filling document templates
- Validating required form fields
- Extracting email addresses
- Generating unique invoice IDs

## Installation
No external dependencies are required for basic usage. Just clone the repository and run the Python script.

## Example Usage
```python
from document_automation_tasks import fill_template, format_document_data

client_data = {
    "first_name": "John",
    "last_name": "Doe",
    "loan_amount": 150000,
    "interest_rate": 5.75,
    "closing_date": "2025-03-06"
}

formatted_data = format_document_data(client_data)
print(formatted_data)
