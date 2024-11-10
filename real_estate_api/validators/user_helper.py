class UserHelper:
    def validate_user(self,request):
        errors = {}

        if request.user.is_anonymous:
            errors['user'] = 'User is not logged in'
            return errors
        if request.user.api_secret_key != request.META.get('HTTP_API_SECRET_KEY'):
            errors['api_secret'] = 'Invalid API secret key'
            return errors
            