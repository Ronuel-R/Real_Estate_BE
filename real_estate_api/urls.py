from django.urls import path
from .versions.v1p0.property.get.get_property_list_views import PropertyListAPI
from .versions.v1p0.property.get.get_property_views import PropertyAPI
from .versions.v1p0.login.login_views import UserLoginView
from .versions.v1p0.property.delete.delete_property_views import DeletePropertyAPI
from .versions.v1p0.property.create.create_property_views import CreatePropertyAPI
from .versions.v1p0.property.update.update_property_views import UpdatePropertyAPI



urlpatterns = [
    path('login/', UserLoginView.as_view(), name = 'client_login'),
    path('property_list/', PropertyListAPI.as_view(), name = 'property_list'),
    path('property/<str:uid>', PropertyAPI.as_view(), name = 'property'),
    path('update/<str:uid>', UpdatePropertyAPI.as_view(), name = 'update_property'),
    path('delete/<str:uid>', DeletePropertyAPI.as_view(), name = 'delete_property'),
    path('create/', CreatePropertyAPI.as_view(), name = 'create_property'),

]