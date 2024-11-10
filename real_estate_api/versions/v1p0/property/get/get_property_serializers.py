from rest_framework import serializers
from real_estate_api.models.property_model import Property

class ListPropertySerializer(serializers.ModelSerializer):
    total_property = serializers.SerializerMethodField()
    total_available_property = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()
    class Meta:
        model = Property
        fields = ['uid', 'property_name', 'location','description', 'property_image',
                  'description','no_of_rooms','no_of_bathroom','no_of_bathroom',
                  'no_of_grid','no_of_garage','posted_date','features','is_available','total_property','total_available_property','price','price_per_sqm']
    
    def get_total_property(self, obj):
        property = Property.objects.all().count()
        return property

    def get_total_available_property(self, obj):
        property = Property.objects.filter(is_available= True).count()
        return property
    
    def get_features(self, obj):
        return obj.features.split(',') if obj.features else []