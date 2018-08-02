from django.urls import path
from . import views

urlpatterns = [
    path('v1/operation_log', views.RecordList.as_view()),
]
