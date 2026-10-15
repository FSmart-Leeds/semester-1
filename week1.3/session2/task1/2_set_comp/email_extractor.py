# Week 1.3, Session 2: Email Extractor

raw_emails = ["UserA@gmail.com", "admin@site.com", "usera@gmail.com", "UserB@yahoo.com", "admin@site.com"]

# set comprehension to extract a clean, unique set of lowercase email addresses
clean_emails = []
for email in raw_emails:
    clean_email = email.lower()
    clean_email = clean_email.split('@')[0]
    if clean_email in clean_emails:
        continue
    clean_emails.append(clean_email)

# print the clean set of email addressed
print(clean_emails)

# Optional - consider the case where some of the emails are not valid (i.e., without the @ in the email address).
# raw_emails2 = ["UserA@gmail.com", "SYSTEM_ALERT", "usera@gmail.com", "admin@site.com", "UserB@yahoo.com"]
# write another set comprehension for this case to extract a clean, unique set of valid, lowercase email addresses
