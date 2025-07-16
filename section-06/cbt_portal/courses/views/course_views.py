from django.http import HttpResponse,JsonResponse
from courses.models.course import Course

def course_list(request):
    courses=Course.objects.all()
    print(type(courses.values()))
    print(courses.values())
    response = {'courses':list(courses.values())}
    return JsonResponse(response)