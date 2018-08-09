from django.urls import path, include

urlpatterns = [
    path('import_export/', include('apps.import_export.urls')),
    path('operation_log', include('apps.transfer.urls')),
]
