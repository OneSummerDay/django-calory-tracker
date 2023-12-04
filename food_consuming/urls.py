from django.urls import path
from food_consuming import views


urlpatterns = [
    path('', views.IndexView, name="index")
]
