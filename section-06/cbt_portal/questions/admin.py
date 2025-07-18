from django.contrib import admin
from .models.exam_question import ExamQuestion
from .models.exam_choice import ExamChoice
admin.site.register(ExamQuestion)
admin.site.register(ExamChoice) 
# Register your models here.
