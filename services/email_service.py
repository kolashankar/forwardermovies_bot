import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import config

class EmailService:
    def send_otp_email(self, recipient_email, otp):
        sender_email = config.EMAIL_SENDER
        password = config.EMAIL_PASSWORD

        message = MIMEMultipart("alternative")
        message["Subject"] = "OTP for Email Verification"
        message["From"] = sender_email
        message["To"] = recipient_email

        text = f"Your OTP for email verification is: {otp}"
        html = f"""
        <html>
          <body>
            <p>Your OTP for email verification is: <strong>{otp}</strong></p>
          </body>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, message.as_string())

