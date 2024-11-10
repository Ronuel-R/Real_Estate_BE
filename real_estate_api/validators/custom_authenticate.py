# from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

# class ApiSecretAuthenticationBackend(ModelBackend):
#     def authenticate(self, request, api_secret_key=None):
#         if not api_secret_key:
#             return None
#         try:
#             user = User.objects.get(api_secret_key=api_secret_key)
#             return user
#         except User.DoesNotExist:
#             return None

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass
        return None
