__author__ = 'hd'

from flask.ext.mail import Message
from app import mail, app
from flask import render_template
from config import ADMINS

from flask import current_app

from .decorators import async


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # mail.send(msg)
    send_async_email(msg)


@async
def send_async_email(msg):
    with app.app_context():
        mail.send(msg)


def follower_notification(followed, follower):
    send_email(subject="[microblog] {0} is following you!".format(follower.nickname),
               sender=ADMINS[0],
               recipients=[followed.email],
               text_body=render_template("follower_email.txt",
                                         user=followed, follower=follower),
               html_body=render_template("follower_email.html",
                                         user=followed, follower=follower)
               )