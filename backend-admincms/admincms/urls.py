from django.urls import path
from .views import AdminCMSView

urlpatterns = [
    path('admincms/', AdminCMSView.as_view(), name='admincms-create'),
]
