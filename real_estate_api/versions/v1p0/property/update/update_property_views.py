from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .update_property_serizializers import UpdatePropertySerializer
from real_estate_api.models.property_model import Property
from real_estate_api.validators.user_helper import UserHelper
from django.core.files.uploadedfile import InMemoryUploadedFile

class UpdatePropertyAPI(APIView):
    def post(self,request,uid):  
        errors = UserHelper.validate_user(self,request)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
        property_instance = Property.objects.get(uid=uid)
        mutable_data = request.data.copy()

        if 'property_image' in request.data and not isinstance(request.FILES.get('property_image'), InMemoryUploadedFile):
            del mutable_data['property_image']

        
        serializer = UpdatePropertySerializer(instance=property_instance, data=mutable_data,partial=True)

        if serializer.is_valid():
            
            serializer.save()

            return Response({'message': 'Success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Failed', 'message': 'Please Recheck Input','data': serializer.data,'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)