import smtplib
from email.mime.text import MIMEText

# EMAIL CONFIG
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
EMAIL_RECEIVER = "receiver_email@gmail.com"

def send_email_alert(file_path):
    try:
        msg = MIMEText(f"File modified: {file_path}")
        msg["Subject"] = "🚨 File Integrity Alert"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)

        print("📧 Email alert sent!")
    except Exception as e:
        print("Email error:", e)


# WHATSAPP (Twilio)
try:
    from twilio.rest import Client

    ACCOUNT_SID = "your_sid"
    AUTH_TOKEN = "your_token"

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_whatsapp_alert(file_path):
        try:
            client.messages.create(
                body=f"🚨 File Modified: {file_path}",
                from_="whatsapp:+14155238886",
                to="whatsapp:+91XXXXXXXXXX"
            )
            print("📱 WhatsApp alert sent!")
        except Exception as e:
            print("WhatsApp error:", e)

except:
    def send_whatsapp_alert(file_path):
        pass


# CLOUD LOGGING (optional)
try:
    import requests

    def send_to_cloud(file_path):
        try:
            requests.post(
                "https://webhook.site/your-url",
                json={"file": file_path, "status": "modified"}
            )
            print("☁️ Cloud log sent!")
        except:
            pass
except:
    def send_to_cloud(file_path):
        pass
