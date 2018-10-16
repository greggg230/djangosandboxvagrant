import os
import sys


sys.path.append("/webapps/djangosandbox/src/djangosandbox")
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'djangosandbox.conf.generic.settings')

import django

django.setup()

from django.contrib.auth.models import User


# Create a user so we can login.
try:
    User.objects.get(username="admin")
except User.DoesNotExist:
    my_user = User(username="admin", email="admin@test.com", is_staff=True)
    my_user.set_password("password123")
    my_user.save()
