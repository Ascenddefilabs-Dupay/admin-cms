from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AdminCMS
from .serializers import AdminCMSSerializer

class AdminCMSView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AdminCMSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountTypeListView(APIView):
    def get(self, request, *args, **kwargs):
        account_types = AdminCMS.objects.exclude(account_type__isnull=True).exclude(account_type__exact='').values_list('account_type', flat=True)
        return Response(list(account_types), status=status.HTTP_200_OK)

class CurrencyTypeListView(APIView):
    def get(self, request, *args, **kwargs):
        currency_types = AdminCMS.objects.exclude(currency_type__isnull=True).exclude(currency_type__exact='').values_list('currency_type', flat=True)
        return Response(list(currency_types), status=status.HTTP_200_OK)
