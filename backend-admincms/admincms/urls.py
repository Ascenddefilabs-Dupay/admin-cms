from django.urls import path
from .views import AdminCMSView, AccountTypeListView, CurrencyTypeListView

urlpatterns = [
    path('admincms/', AdminCMSView.as_view(), name='admincms-create'),  # For adding data
    path('admincms/account/', AccountTypeListView.as_view(), name='admincms-account-types'),  # For fetching account types
    path('admincms/<int:pk>/', AdminCMSView.as_view(), name='admincms-detail'),  # For fetching, updating, and deleting individual items
    path('admincms/currency/', CurrencyTypeListView.as_view(), name='admincms-currency-types'),  # For fetching currency types
]