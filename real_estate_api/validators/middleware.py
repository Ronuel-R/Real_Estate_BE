from django.utils.deprecation import MiddlewareMixin

class CustomCORSMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Headers'] = 'http_api_secret_key'
        return response