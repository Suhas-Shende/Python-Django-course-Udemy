from django.db.models import *
from courses.models.course import Course
class Exam(Model):
    course=ForeignKey(Course, on_delete=CASCADE)
    title=CharField(max_length=100)
    total_marks=IntegerField()
    date=DateTimeField()
    duration_minutes=IntegerField()

    def __str__(self):
        return f"{self.title}"