from django.urls import path
from .views import (
    home,
    letter
)
app_name = 'sunflower'
urlpatterns = [
    path('', home, name='home'),
    path('letter/', letter, name='letter')
]