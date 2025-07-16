from django.http import HttpResponse,JsonResponse
from courses.models.course import Course
from rest_framework.parsers import JSONParser
from courses.serializers.course_serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *

@api_view(['GET','POST'])
def course_list(request):
    if request.method == 'GET':
        courses=Course.objects.all()
        serializer=CourseSerializer(courses,many=True)
        # response = {'courses':list(courses.values())}
        response={
            'courses':serializer.data
        }
    
        return Response(response,status=HTTP_200_OK)
    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def course_detail(request,pk):
    courses=get_object_or_404(Course,pk=pk)
    if request.method=='GET':
        
        serializer=CourseSerializer(courses)
        # response = {'courses':list(courses.values())}
        response={
            'courses':serializer.data
        }
    
        return Response(response,status=HTTP_200_OK)
    elif request.method=="PUT":
        
        serializer=CourseSerializer(courses,data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        courses.delete()
        return Response({'Course':'Deleted Successfully'},status=HTTP_204_NO_CONTENT)