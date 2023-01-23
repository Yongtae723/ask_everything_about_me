# send_gmail.py：

import smtplib
import ssl
from email.mime.text import MIMEText
from typing import Tuple

from ask_everything_about_me.config import settings


def send_gmail(subject: str, body: str, email_address: str) -> Tuple[bool, str]:
    try:
        msg = MIMEText(body + f"\n Email : {email_address}", "html")
        msg["Subject"] = "【Ask Everything About Me】 " + subject
        msg["To"] = settings.gmail_account
        msg["From"] = settings.gmail_account

        # Gmailに接続
        server = smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, context=ssl.create_default_context()
        )
        server.login(settings.gmail_account, settings.gmail_password)
        server.send_message(msg)  # メールの送信
        return (True, "Successfully send E-mail")

    except Exception as e:
        return (False, f"error with {e}")
