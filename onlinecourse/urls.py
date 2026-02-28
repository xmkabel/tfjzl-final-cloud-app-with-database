from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    path(route='', view=views.CourseListView.as_view(), name='index'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # Add these two lines below:
    path('<int:course_id>/submit/', views.submit, name='submit'),
    path('course/<int:course_id>/submission/<int:submission_id>/show_exam_result/', 
         views.show_exam_result, name='show_exam_result'),

    # <HINT> Create a route for submit view

    # <HINT> Create a route for show_exam_result view

 ]
