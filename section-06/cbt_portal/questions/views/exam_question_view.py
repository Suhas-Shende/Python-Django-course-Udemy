

from questions.serializers.exam_question_serializer import ExamQuestionSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from questions.models.exam_question import ExamQuestion

class ExamQuestionView(APIView):
    
    def get(self,request,format=None):
        courses=ExamQuestion.objects.all()
        serializer=ExamQuestionSerializer(courses,many=True)
        # response = {'courses':list(courses.values())}
        response={
            'courses':serializer.data
        }
    
        return Response(response,status=HTTP_200_OK) 
    
    def post(self,request,format=None):
        serializer = ExamQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    

class ExamQuestionDetailUpdateDeleteView(APIView):
    def get(self,request,pk,format=None):
        courses=get_object_or_404(ExamQuestion,pk=pk)
        serializer=ExamQuestionSerializer(courses)
        # response = {'courses':list(courses.values())}
        response={
            'courses':serializer.data
        }
    
        return Response(response,status=HTTP_200_OK)
    
    def put(self,request,pk,format=None):
        courses=get_object_or_404(ExamQuestion,pk=pk)
        serializer=ExamQuestionSerializer(courses,data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)        

    def delete(self,request,pk,format=None):
        courses=get_object_or_404(ExamQuestion,pk=pk)
        courses.delete()
        return Response({'Course':'Deleted Successfully'},status=HTTP_204_NO_CONTENT)