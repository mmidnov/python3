# okurmen/urls.py
import statistics
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import DownloadReceiptView, home, teachers, groups, students,student_details,managers,managers_details,set_language

urlpatterns = [
    path('', home, name='home'),
    path('teachers/', teachers, name='teachers'),
    path('groups/', groups, name='groups'),
    path('students/', students, name='students'),
    path('managers/', managers, name='managers'),
    path('managers/set-language/', managers, name='managers'),
    path('students/<int:student_id>/', student_details, name='student_details'),
    path('managers/<int:manager_id>/', managers_details, name='managers_details'),
    path('set-language/', set_language, name='set_language'),
    path('students/<int:student_id>/download-receipt/', DownloadReceiptView.as_view(), name='download_receipt'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)