from django.urls import path
from ideKAMI.views import *
app_name = 'ideKAMI'

urlpatterns = [
    path('', show_ide, name='show_ide'),
    path('create-ide/', create_ide, name='create_ide'),
]