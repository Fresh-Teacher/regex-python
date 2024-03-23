import re

text = """
Name: John Doe
Email: john.doe@example.com
Phone: +1 (123) 456-7890
Credit Card:t 1234 5678 9012 3456
"""

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
phone_pattern = r"\+?\d{1,4}[-.() \d]*\d"
credit_card_pattern = r"\b(?:\d[ -]*?){13,16}\b"

redacted_text = re.sub(email_pattern, "[REDACTED_EMAIL]", text)
redacted_text = re.sub(phone_pattern, "[REDACTED_PHONE]", redacted_text)
redacted_text = re.sub(credit_card_pattern, "[REDACTED_CC]", redacted_text)

print("Redacted text:")
print(redacted_text)
