import smtplib
import json
from email.mime.text import MIMEText


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


config = load_config()
smtp_server = config["smtp_server"]
smtp_port = config["smtp_port"]
sender_email = config["sender_email"]
sender_password = config["sender_password"]
recipient_email = config["recipient_email"]
i = 0
subject = f"Sean Test {i}"
body = f"Sean Test {i}"
msg = MIMEText(body)
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject


try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        for i in range(100):
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Email {i+1} sent.")

except Exception as e:
    print(f"Error: {e}")
