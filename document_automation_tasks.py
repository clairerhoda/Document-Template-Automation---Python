from datetime import datetime
import re
import random

# 1. Formatting Data for Document Templates
def format_document_data(data):
    formatted_data = {
        "Full Name": f"{data.get('first_name', '').capitalize()} {data.get('last_name', '').capitalize()}",
        "Loan Amount": f"${data.get('loan_amount', 0):,.2f}",
        "Interest Rate": f"{data.get('interest_rate', 0):.2f}%",
        "Closing Date": datetime.strptime(data.get("closing_date", ""), "%Y-%m-%d").strftime("%m/%d/%Y") if data.get("closing_date") else "N/A"
    }
    return formatted_data

# 2. Auto-Filling a Document Template
def fill_template(template, data):
    return template.format(**data)

# 3. Validating Required Fields in a Form Submission
def check_missing_fields(form_data, required_fields):
    return [field for field in required_fields if not form_data.get(field)]

# 4. Extracting Email Addresses from Text
def extract_emails(text):
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# 5. Generating a Unique Invoice ID
def generate_invoice_id():
    date_part = datetime.now().strftime("%Y%m%d")
    random_part = random.randint(1000, 9999)
    return f"INV-{date_part}-{random_part}"

# Example Data
template = "Dear {client_name},\nYour loan of {loan_amount} has been approved. Your interest rate is {interest_rate}."
client_data = {
    "first_name": "john",
    "last_name": "doe",
    "loan_amount": 150000,
    "interest_rate": 5.75,
    "closing_date": "2025-03-06"
}
form_data = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "phone": "",
    "loan_amount": "100000"
}
required_fields = ["name", "email", "phone", "loan_amount"]
text = "Please contact John at john.doe@example.com or Jane at jane_smith@workmail.com for further details."
data = {
    "client_name": "Jane Smith",
    "loan_amount": "$200,000",
    "interest_rate": "4.5%"
}

# Running Examples
print(format_document_data(client_data))
print(fill_template(template, data))
print(check_missing_fields(form_data, required_fields))
print(extract_emails(text))
print(generate_invoice_id())
