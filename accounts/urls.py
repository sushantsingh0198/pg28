from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('add_class/', views.add_class, name='add_class'),
    path('import_class_detail/',views.import_class_detaail, name= 'import_class_detail'),
    path('remove_class/', views.remove_class, name='remove_class'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('import_teacher_detail/', views.import_teacher_detail, name='import_teacher_detail'),
    path('remove_teacher/', views.remove_teacher, name='remove_teacher'),
    path('view_load_list/', views.view_load_list, name='view_load_list'),
    path('view_individual/', views.viwe_individual, name='view_individual')
]
