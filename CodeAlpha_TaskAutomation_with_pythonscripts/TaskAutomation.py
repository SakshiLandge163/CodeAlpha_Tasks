import re
with open("input.txt","r") as file:
    text = file.read()
    
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
with open("output_emails.txt","w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email extraction completed successfully!")