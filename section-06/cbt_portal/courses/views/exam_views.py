
from courses.models.exam import Exam
from courses.serializers.exam_serializers import ExamSerializer
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.generics import GenericAPIView,CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView



# Class based view based on inheritance of generic and mixins which extends CreateModelMixin,ListModelMixin which is Concrete View Classes
# it is mixture ListAPIView=GenericAPIView +ListModelMixin
#https://www.django-rest-framework.org/api-guide/generic-views/
class ExamCreateListView(CreateAPIView,ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer



class ExamDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer




# Class based view based on inheritance of generic and mixins
# class ExamCreateListView(ListModelMixin,CreateModelMixin,GenericAPIView):
#     queryset = Exam.objects.all()
#     serializer_class = ExamSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

        



'''ExamCreatelistview by the use of APIView'''
# class ExamCreateListView(APIView):
#     def get(self,request,format=None):
#         exam=Exam.objects.all()
#         serializers=ExamSerializer(exam,many=True,context={'request': request})
#         return Response(serializers.data,status=HTTP_200_OK)


#     def post(self,request,Format=None):
#         serializers=ExamSerializer(data=request.data,context={'request': request})
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=HTTP_201_CREATED)
#         return Response(serializers.errors,status=HTTP_400_BAD_REQUEST)
    



# class ExamDetailUpdateDeleteView(APIView):
#     def get(self,request,pk):
#         exam=get_object_or_404(Exam,pk=pk)
#         serializers=ExamSerializer(exam,context={'request': request})
#         return Response(serializers.data,status=HTTP_200_OK)


#     def put(self,request,pk):
#         exam=get_object_or_404(Exam,pk=pk)
#         serializers=ExamSerializer(exam,data=request.data,context={'request': request})
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=HTTP_201_CREATED)
#         return Response(serializers.errors,status=HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         exam=get_object_or_404(Exam,title=pk)
#         exam.delete()
#         return Response({'exam':'Exam deleed successsfully'},status=HTTP_410_GONE)