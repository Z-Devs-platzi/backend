"""Celery tasks."""

# Django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

# Models
from eventup.users.models import User
# from eventup.rides.models import Ride

# Celery
from celery.decorators import task
# from celery.decorators import task, periodic_task

# Utilities
import jwt
# import time
from datetime import timedelta


def gen_verification_token(user):
    """Create JWT token that the user can use to verify its account."""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        'user': user.username,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation'
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token.decode()


@task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(email):
    """Send account verification link to given user."""
    print("..**" * 40)
    user = User.objects.get(email=email)
    print(email)
    print(user.email)
    print("..**" * 40)

    verification_token = gen_verification_token(user)
    subject = 'Welcome @{}! Verify your account to start using Event Up'.format(user.username)
    from_email = 'Event Up <mailgun@mg.event-up.digital>'
    content = render_to_string(
        'emails/users/account_verification.html',
        {'token': verification_token, 'user': user}
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [email])
    msg.attach_alternative(content, "text/html")
    msg.send()


# Can be with cron tab rules (cronjobs * * * * 10)
# @periodic_task(name='disable_finished_rides', run_every=timedelta(minutes=20))
# def disable_finished_rides():
#     """Disable finished rides."""
#     now = timezone.now()
#     offset = now + timedelta(minutes=20)

#     # Update rides that have already finished
#     rides = Ride.objects.filter(
#         arrival_date__gte=now,
#         arrival_date__lte=offset,
#         is_active=True
#     )
#     rides.update(is_active=False)
