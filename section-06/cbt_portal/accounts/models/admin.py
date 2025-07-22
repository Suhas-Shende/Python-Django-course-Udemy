from accounts.models.user import CBTCustomUser
from django.db.models import OneToOneField,CharField,Model,CASCADE


class Admin(Model):
    user=OneToOneField(CBTCustomUser,on_delete=CASCADE)
    department=CharField(max_length=100)
    def __str__(self):
        return self.user.username
    