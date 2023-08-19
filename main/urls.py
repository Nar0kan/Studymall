from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', redirect_to_home_page, name='redirect_home'),
    path('home/', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('about/', about_page, name='about'),
    path('study/', study_programs_page, name='study_programs'),
    path('study/python/', python_study_plan_page, name='python_study_plan'),
]
