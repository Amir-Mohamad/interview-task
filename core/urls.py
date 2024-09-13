# app/urls.py

from django.urls import path
from .views import TitanicUploadView, TitanicListView, TitanicUpdateView

app_name = "core"
urlpatterns = [
    path('', TitanicListView.as_view(), name='index'),
    path('upload/', TitanicUploadView.as_view(), name='upload'),
    path('edit/<int:pk>/', TitanicUpdateView.as_view(), name='edit'),
]
