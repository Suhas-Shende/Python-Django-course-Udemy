from django.contrib import admin

# Register your models here.
from accounts.models.students import Student
from accounts.models.admin import Admin
from accounts.models.user import CBTCustomUser

admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(CBTCustomUser)
