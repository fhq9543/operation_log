from django.urls import path
from . import views

urlpatterns = [
    path('import', views.ImportView.as_view()),
    path('export', views.ExportView.as_view()),
]
