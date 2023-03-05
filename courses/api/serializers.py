from rest_framework import serializers
from courses.models import Subject, Course, Module

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']
        
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['order', 'title', 'description']
class CourseSerializer(serializers.ModelSerializer):
    #many=True: we are serializing multiple objects, read_only: should not be included in any input
    modules = ModuleSerializer(many=True, read_only=True)
    class Meta:
        model = Course   
        fields = ['id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules']
        
        
