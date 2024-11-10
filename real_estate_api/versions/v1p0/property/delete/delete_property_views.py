from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from real_estate_api.models.property_model import Property

class DeletePropertyAPI(APIView):
    def post(self,request, uid):
        property = Property.objects.get(uid=uid)
        property.is_available=False
        property.save()
        return Response({'message': 'Success'}, status=status.HTTP_200_OK)