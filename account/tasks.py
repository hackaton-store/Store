from django.core.mail import send_mail
from django.conf import settings
from store.celery import app
from .utilities import send_activation_code
from django.contrib.auth import get_user_model

User = get_user_model()


@app.task
def send_activation_code_task(user_id):
    user = User.objects.get(id=user_id)
    send_activation_code(user)
    