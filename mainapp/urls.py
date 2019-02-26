from django.urls import path
from .views import main_view, upload_image, get_picture

app_name = 'mainapp'

urlpatterns = [
    path('', main_view, name='main'),
    path('upload/', upload_image, name='upload'),
    path('<int:pk>/', get_picture, name='get_picture'),
]