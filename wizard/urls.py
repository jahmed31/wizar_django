from django.urls import path
from .views import *


urlpatterns = [
    path('create/', CreateBooking.as_view()),
    path('', ProductList.as_view()),
]
