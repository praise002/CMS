from courses.api.serializers import SubjectSerializer
from courses.models import Subject, Course
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
class SubjectDetailView(generics.RetrieveAPIView):  #has a pk 
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
class CourseEnrollView(APIView):
    def post(self, request, pk, format=None):  #for post actions
        course = get_object_or_404(Course, pk=pk)  #contain id of a course, course is retrieved by the pk
        course.students.add(request.user)  #add the current user
        return Response({'enrolled': True})