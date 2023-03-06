from courses.api.serializers import SubjectSerializer, CourseSerializer
from courses.models import Subject, Course
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
class SubjectDetailView(generics.RetrieveAPIView):  #has a pk 
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
# class CourseEnrollView(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]  #only authenticated users
    
#     def post(self, request, pk, format=None):  #for post actions
#         course = get_object_or_404(Course, pk=pk)  #contain id of a course, course is retrieved by the pk
#         course.students.add(request.user)  #add the current user
#         return Response({'enrolled': True})
    
    
class CourseViewSet(viewsets.ReadOnlyModelViewSet):  #provides default list() and retrieve() actions
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    @action(detail=True,  #action is to be performed on a single obj
            methods=['post'], 
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})