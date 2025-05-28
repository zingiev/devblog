import os
from django.http import Http404
from dotenv import load_dotenv


load_dotenv()


class HiddenUrlAdmin:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_ips = [ip.strip() for ip in os.getenv(
            'ALLOWED_ADMIN_IPS', '127.0.0.1').split(',')]

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            client_ip = request.META.get('REMOTE_ADDR')

            if client_ip not in self.allowed_ips:
                raise Http404
        return self.get_response(request)
