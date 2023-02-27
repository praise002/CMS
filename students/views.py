from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from courses.models import Course
from . forms import CourseEnrollForm


class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')  #redirect the user after successful submission
    
    def form_valid(self, form):  #executed when valid form data has been posted: override it to log user in when dey sign up
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        login(self.request, user)
        return result
    
class StudentEnrollCourseView(LoginRequiredMixin, FormView):  
    #LoginRequiredMixin(so that only log-in users can access d view)
    #FormView(to handle form submission)
    course = None   #to store the given course obj  
    form_class = CourseEnrollForm
    
    def form_valid(self, form):
        #If valid add student enrolled on the course
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])  #redirect the enrolled student to registered courses
    
    
class StudentCourseListView(LoginRequiredMixin, ListView):
    # A view to see courses that students are enrolled in
    model = Course   
    template_name = 'students/course/list.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])


class StudentCourseDetailView(DetailView):
    model = Course   
    template_name = 'students/course/detail.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get course object
        course = self.get_object()
        if 'module_id' in self.kwargs:
            # get current module
            context['module'] = course.modules.get(id=self.kwargs['module_id'])
        else:
            # get first module
            context['module'] = course.modules.all()[0]
        return context