
from courses.models.exam import Exam
from courses.serializers.exam_serializers import ExamSerializer
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class ExamCreateListView(APIView):
    def get(self,request,format=None):
        exam=Exam.objects.all()
        serializers=ExamSerializer(exam,many=True,context={'request': request})
        return Response(serializers.data,status=HTTP_200_OK)


    def post(self,request,Format=None):
        serializers=ExamSerializer(data=request.data,context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=HTTP_201_CREATED)
        return Response(serializers.errors,status=HTTP_400_BAD_REQUEST)
    



class ExamDetailUpdateDeleteView(APIView):
    def get(self,request,pk):
        exam=get_object_or_404(Exam,pk=pk)
        serializers=ExamSerializer(exam,context={'request': request})
        return Response(serializers.data,status=HTTP_200_OK)


    def put(self,request,pk):
        exam=get_object_or_404(Exam,pk=pk)
        serializers=ExamSerializer(exam,data=request.data,context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=HTTP_201_CREATED)
        return Response(serializers.errors,status=HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        exam=get_object_or_404(Exam,title=pk)
        exam.delete()
        return Response({'exam':'Exam deleed successsfully'},status=HTTP_410_GONE)