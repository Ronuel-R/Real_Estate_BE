from django.urls import path
from .versions.v1p0.property.get.get_property_views import ListPropertyAPI
from .versions.v1p0.login.login_views import UserLoginView
from .versions.v1p0.property.delete.delete_property_views import DeletePropertyAPI
from .versions.v1p0.property.create.create_property_views import CreatePropertyAPI



urlpatterns = [
    path('login/', UserLoginView.as_view(), name = 'client_login'),
    path('property_list/', ListPropertyAPI.as_view(), name = 'property_list'),
    path('delete/', DeletePropertyAPI.as_view(), name = 'delete_property'),
    path('create/', CreatePropertyAPI.as_view(), name = 'create_property'),

]