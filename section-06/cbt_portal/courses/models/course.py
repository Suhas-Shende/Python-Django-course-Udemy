from django.db.models import *

class Course(Model):
    name=CharField(max_length=100)
    code=CharField(max_length=10, unique=True)
    description=CharField(max_length=500)

    def __str__(self):
        return f"{self.name} {self.code}"