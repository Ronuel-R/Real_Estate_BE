from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .create_property_serializers import CreatePropertySerializer
from real_estate_api.models.property_model import Property
from real_estate_api.validators.user_helper import UserHelper

class CreatePropertyAPI(APIView):
    def post(self,request):  
        errors = UserHelper.validate_user(self,request)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CreatePropertySerializer(data = request.data)

        if serializer.is_valid():
            features_list = request.data.get('features', [])
            features = ",".join(features_list)

            property = Property.objects.create(
            property_name= request.data['property_name'],   
            location= request.data['location'],   
            description= request.data['description'],   
            property_image= request.FILES['property_image'],     
            no_of_rooms= request.data['no_of_rooms'],   
            no_of_bathroom = request.data['no_of_bathroom'],     
            no_of_grid= request.data['no_of_grid'],   
            no_of_garage= request.data['no_of_garage'],   
            posted_date= request.data['posted_date'],   
            price= request.data['price'],   
            price_per_sqm= request.data['price_per_sqm'],   
            features=features,   
            )
            return Response({'message': 'Success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Failed', 'message': 'Please Recheck Input','data': serializer.data}, status=status.HTTP_400_BAD_REQUEST)
