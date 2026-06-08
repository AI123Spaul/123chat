import re

def is_valid_email(email):
# Define a basic email pattern
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
return re.match(pattern, email) is not None

def validate_emails(email_list):
valid_emails = []
invalid_emails = []

for email in email_list:
if is_valid_email(email):
valid_emails.append(email)
else:
invalid_emails.append(email)

return valid_emails, invalid_emails

# Main program
if __name__ == "__main__":
emails = [
"john.doe@example.com",
"jane_doe123@domain.org",
"invalid-email@.com",
"noatsign.com",
"hello@sub.domain.co",
"user@@doubleat.com",
"suvadip@hotmail.com",
"paul@1111"
]

valid, invalid = validate_emails(emails)

print("✅ Valid Emails: as per Suvadip")
for v in valid:
print(f" {v}")

print("\n❌ Invalid Emails: as per Suvadip")
for i in invalid:
print(f" {i}")