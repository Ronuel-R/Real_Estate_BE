from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .get_property_serializers import ListPropertySerializer
from real_estate_api.models.property_model import Property

class PropertyAPI(APIView):
    def get(self,request,uid):  
        property = Property.objects.get(uid=uid,is_available = True)
        serializer = ListPropertySerializer(property)

        return Response({'message': 'Success', 'data': serializer.data}, status=status.HTTP_200_OK)