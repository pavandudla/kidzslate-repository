from django.core.mail import send_mail
import random
from django.config import settings



def send_otp_via_email(email):
    subject = 'your account verification email'
    otp = random.randint(1000,9999)
    message = f'your otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])