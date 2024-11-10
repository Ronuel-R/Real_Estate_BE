from rest_framework import serializers
from real_estate_api.models.property_model import Property

class UpdatePropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = ['property_name', 'location','description', 'property_image','no_of_rooms','no_of_bathroom',
                  'no_of_grid','no_of_garage','posted_date','features','price','price_per_sqm']
