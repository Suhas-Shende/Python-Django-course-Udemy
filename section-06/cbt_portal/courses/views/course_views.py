from django.http import HttpResponse,JsonResponse
from courses.models.course import Course
from rest_framework.parsers import JSONParser
from courses.serializers.course_serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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
    


class CourseListView(APIView):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses,many=True,context={'request': request})
        # response = {'courses':list(courses.values())}
        response={
            'courses':serializer.data
        }
    
        return Response(response,status=HTTP_200_OK) 
    
    def post(self,request,format=None):
        serializer = CourseSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    

class CourseDetailUpdateDeleteView(APIView):
    def get(self,request,pk,format=None):
        courses=get_object_or_404(Course,pk=pk)
        serializer=CourseSerializer(courses,context={'request': request})
        # response = {'courses':list(courses.values())}
        response={
            'courses':serializer.data
        }
    
        return Response(response,status=HTTP_200_OK)
    
    def put(self,request,pk,format=None):
        courses=get_object_or_404(Course,pk=pk)
        serializer=CourseSerializer(courses,data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)        

    def delete(self,request,pk,format=None):
        courses=get_object_or_404(Course,pk=pk)
        courses.delete()
        return Response({'Course':'Deleted Successfully'},status=HTTP_204_NO_CONTENT)
    


''' Below is another method to show view and this called viewset'''
class CourseViewSet(ViewSet):
    """A simple ViewSet for listing or retrieving users"""
    def list(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Course.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(user,context={'request': request})
        return Response(serializer.data)