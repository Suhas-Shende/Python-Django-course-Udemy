# from django.http import HttpResponse,JsonResponse
# from courses.models.course import Course

# def course_list(request):
#     courselist=Course.objects.all()
#     return HttpResponse(" ".join([str(course) for course in courselist]))