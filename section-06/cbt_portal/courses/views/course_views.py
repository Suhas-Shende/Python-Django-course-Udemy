from django.http import HttpResponse,JsonResponse
from courses.models.course import Course
from courses.serializers.course_serializers import CourseSerializer
from django.shortcuts import get_object_or_404


def course_list(request):
    courses=Course.objects.all()
    serializer=CourseSerializer(courses,many=True)
    # response = {'courses':list(courses.values())}
    response={
        'courses':serializer.data
    }
  
    return JsonResponse(response,safe=False)


def course_detail(request,pk):
    courses=get_object_or_404(Course,pk=pk)
    serializer=CourseSerializer(courses)
    # response = {'courses':list(courses.values())}
    response={
        'courses':serializer.data
    }
  
    return JsonResponse(response,safe=False)
    