from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('type/<int:type_id>/', category, name='type_detail'),
    path('flower/<int:flower_id>/,', flower, name='flower_detail')
]