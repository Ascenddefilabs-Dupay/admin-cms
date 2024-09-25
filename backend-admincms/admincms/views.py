from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AdminCMS
from .serializers import AdminCMSSerializer

class AdminCMSView(APIView):
    parser_classes = [MultiPartParser, FormParser]  # Add parsers for file upload

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            try:
                item = AdminCMS.objects.get(pk=kwargs['pk'])
                serializer = AdminCMSSerializer(item)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except AdminCMS.DoesNotExist:
                return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            items = AdminCMS.objects.all()
            serializer = AdminCMSSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = AdminCMSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            item = AdminCMS.objects.get(pk=kwargs['pk'])
            serializer = AdminCMSSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Data updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AdminCMS.DoesNotExist:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            item = AdminCMS.objects.get(pk=kwargs['pk'])
            item.delete()
            return Response({"message": "Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except AdminCMS.DoesNotExist:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

class AccountTypeListView(APIView):
    def get(self, request, *args, **kwargs):
        account_types = AdminCMS.objects.exclude(account_type__isnull=True).exclude(account_type__exact='').values('id', 'account_type')
        return Response(account_types, status=status.HTTP_200_OK)

class CurrencyTypeListView(APIView):
    def get(self, request, *args, **kwargs):
        currency_types = AdminCMS.objects.exclude(currency_type__isnull=True).exclude(currency_type__exact='').values('id', 'currency_type')
        return Response(currency_types, status=status.HTTP_200_OK)