from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField

class CBTCustomUser(AbstractUser):
    is_student=BooleanField(default=False)
    is_admin=BooleanField(default=False)

    def __str__(self):
        return self.username
