import re

email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

with open('email_list.txt', 'r') as input_file:
    email_addresses = input_file.readlines()

invalid_emails = [email.strip() for email in email_addresses if not email_pattern.match(email.strip())]

with open('invalid_emails.txt', 'w') as output_file:
    for invalid_email in invalid_emails:
        output_file.write(f"{invalid_email}\n")
