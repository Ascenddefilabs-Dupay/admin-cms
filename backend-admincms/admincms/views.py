# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from rest_framework.exceptions import MethodNotAllowed
# # from .models import AdminCMS
# # from .serializers import AdminCMSSerializer

# # class AdminCMSView(APIView):
# #     def get(self, request, *args, **kwargs):
# #         raise MethodNotAllowed(method='GET')
        

# #     def post(self, request, *args, **kwargs):
# #         serializer = AdminCMSSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response({"message": "Added successfully"}, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class AdminCMSView(APIView):
#     def post(self, request, *args, **kwargs):
#         # Handle POST request
#         return Response({"message": "POST request handled"}, status=status.HTTP_200_OK)
    
#     def put(self, request, *args, **kwargs):
#         # Handle PUT request
#         return Response({"message": "PUT request handled"}, status=status.HTTP_200_OK)
    
#     def delete(self, request, *args, **kwargs):
#         # Handle DELETE request
#         return Response({"message": "DELETE request handled"}, status=status.HTTP_200_OK)

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
            return Response({"message": "Data added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
