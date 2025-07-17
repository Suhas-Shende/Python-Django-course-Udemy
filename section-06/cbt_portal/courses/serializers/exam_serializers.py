from rest_framework.serializers import *
from courses.models.exam import Exam
from courses.serializers.course_serializers import CourseSerializer
class ExamSerializer(Serializer):
    course=CourseSerializer(read_only=True)
    course_id=IntegerField()
    title=SlugField()
    total_marks=IntegerField()
    date=DateTimeField()
    duration_minutes=IntegerField()

# serializer for Exam model to convert to JSON
#serializer means model coversion to JSON



    def create(self, validated_data):
 
        """Create and return a new `Snippet` instance, given the validated data. """
   
        return Exam.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        
        instance.title = validated_data.get('title', instance.title)
        instance.total_marks = validated_data.get('total_marks', instance.total_marks)
        instance.date= validated_data.get('date', instance.date)
        instance.duration_minutes = validated_data.get('duration_minutes', instance.duration_minutes)
        instance.save()
        return instance