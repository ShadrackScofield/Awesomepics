from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('dogs/', view_dogs, name='dogs'),
    path('tech/', view_tech, name='tech'),
    path('new/pictures/', upload_pictures, name='newPics'),
    path('details/', details, name='details'),

]
