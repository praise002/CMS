# An E-learning platform
- pipenv install Django~=4.1.0
- pipenv install Pillow==9.2.0
- django-admin startproject educa .
- django-admin startapp courses
- pipenv install python-dotenv
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
- python manage.py dumpdata courses --indent=2
- python manage.py dumpdata --help
- python manage.py dumpdata courses --indent=2 --output=courses/fixtures/subjects.json
- python manage.py loaddata subjects.json
- python manage.py shell
- python manage.py runserver
- pipenv install django-debug-toolbar
- pipenv install django-braces==1.15.0

- pipenv install django-embed-video==1.4.4

- I learned how to use fixtures to provide initial data for models. By using model inheritance, you created a flexible system to    manage different types of content for the course modules. I also implemented a custom model field on order objects and created an authentication system for the e-learning platform.
- I learned how to use class-based views and mixins to create a content management 
system. I also worked with groups and permissions to restrict access to your views. I learned 
how to use formsets and model formsets to manage course modules and their content. I also built 
a drag-and-drop functionality with JavaScript to reorder course modules and their contents.