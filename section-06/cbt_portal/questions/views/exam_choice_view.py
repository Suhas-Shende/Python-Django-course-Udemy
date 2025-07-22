
from courses.models.course import Course
from courses.serializers.course_serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from questions.models.exam_choice import ExamChoice
from questions.serializers.exam_choice_serializer import ExamChoiceSerializer


class ExamChoiceView(APIView):
    
    def get(self,request,pk,format=None):
        courses=ExamChoice.objects.filter(question_id=pk)
        serializer=ExamChoiceSerializer(courses,many=True)
        # response = {'courses':list(courses.values())}
     
        return Response(serializer.data,status=HTTP_200_OK) 
    
    def post(self,request,format=None):
        serializer = ExamChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    





class ExamChoiceDetailUpdateDeleteView(APIView):
    def get(self,request,pk,format=None):
        courses=get_object_or_404(ExamChoice,pk=pk)
        serializer=ExamChoiceSerializer(courses)
        # response = {'courses':list(courses.values())}
        response={
            'courses':serializer.data
        }
    
        return Response(response,status=HTTP_200_OK)
    
    def put(self,request,pk,format=None):
        courses=get_object_or_404(ExamChoice,pk=pk)
        serializer=ExamChoiceSerializer(courses,data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)        

    def delete(self,request,pk,format=None):
        courses=get_object_or_404(ExamChoice,pk=pk)
        courses.delete()
        return Response({'Status':'Deleted Successfully Exam Choice'},status=HTTP_204_NO_CONTENT)