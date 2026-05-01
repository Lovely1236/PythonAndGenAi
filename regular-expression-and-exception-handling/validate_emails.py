import re
def validate_emails(emails):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    for email in emails:
        try:
            if re.match(pattern, email):
                print(f"Valid: {email}")
            else:
                raise ValueError("Invalid email")
        except ValueError:
            print(f"Invalid: {email}")
validate_emails(["alex@corp.com", "wrong.email@"])