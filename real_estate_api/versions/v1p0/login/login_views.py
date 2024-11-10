from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .login_serializers import UserLoginSerializer
from real_estate_api.validators.custom_authenticate import EmailBackend

class UserLoginView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid:

            email = request.data['email']
            password = request.data['password']
            
            user = EmailBackend.authenticate(EmailBackend,request,email=email, password=password)

            if user is None:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
        
            response_data = {
                'message': 'Success',
                'api_secret': user.api_secret_key,
                'access_token': access_token,
            }
            response = JsonResponse(response_data, status=status.HTTP_200_OK)
            response['HTTP_API_SECRET_KEY'] = user.api_secret_key
            
            response['Authorization'] = 'Bearer {}'.format(access_token)

            return response
        
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)