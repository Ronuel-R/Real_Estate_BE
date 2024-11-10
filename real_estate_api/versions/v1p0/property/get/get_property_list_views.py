from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .get_property_serializers import ListPropertySerializer
from real_estate_api.models.property_model import Property

class PropertyListAPI(APIView):
    def get(self,request):  
        property = Property.objects.filter(is_available = True)
        serializer = ListPropertySerializer(property,many=True)

        return Response({'message': 'Success', 'data': serializer.data}, status=status.HTTP_200_OK)