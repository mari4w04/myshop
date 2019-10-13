from celery import task
# from django.core.mail import send_mail
from .models import Order
import smtplib

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    # orderEmail = Order.objects.get(id=order_email)
    # to = orderEmail
    # gmail_user = email from
    # gmail_pwd = pwd
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: PETZ Order Confirmation #{}'.format(order.id)
    print(header)
    # message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    subject = 'PETZ Order Confirmation #{}'.format(order.id)
    text = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}. \nYou will shorty receive an email containing information about tracking your parcel and shipping time.\n\nThank you for choosing us!'.format(order.first_name,order.id)
    message = 'Subject: {}\n\n{}'.format(subject, text)
    smtpserver.sendmail(gmail_user, to, message)
    print('Done!')
    smtpserver.close()