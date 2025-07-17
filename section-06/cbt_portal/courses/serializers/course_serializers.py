from rest_framework.serializers import *
from courses.models.course import Course
from rest_framework.validators import UniqueValidator,UniqueTogetherValidator

class CourseSerializer(Serializer):
    id=IntegerField(read_only=True)
    name=CharField(max_length=100,
                    validators=[UniqueValidator(queryset=Course.objects.all(),message="Name must be unique")]      
                   )
    code=CharField(max_length=20,
                   
                   validators=[UniqueValidator(queryset=Course.objects.all(),message="Code must be unique")]
                   
                   )
    description=CharField(max_length=500,allow_blank=True)
    # class Meta:
       
    #     # by the 'position' field. No two items in a given list may share
    #     # the same position.
    #     validators = [
    #         UniqueTogetherValidator(
    #             queryset=Course.objects.all(),
    #             fields=['name', 'code'],
    #             message="Name and code must be Unique Together"
    #         )
    #     ]

    #Function based validator
    def validate_description(self,value):
        """"Check if there presence of word shit and fuck the if present raise the error"""
        if value.count("Shit") or value.count("Fuck"):
            raise ValidationError("Please Replace Shit or Fuck in field,Enter valid Description")
        return value
        
    def create(self, validated_data):
 
        """Create and return a new `Snippet` instance, given the validated data. """
   
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance