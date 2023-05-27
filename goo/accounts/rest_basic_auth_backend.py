from django.contrib.auth import get_user_model
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed

class EmailBasicAuthentication(BasicAuthentication):
    def authenticate(self, request):
        # Get the credentials from the request headers
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None

        # Extract the credentials from the auth header
        try:
            auth_type, credentials = auth_header.split(' ')
            credentials = base64.b64decode(credentials).decode('utf-8')
            email, password = credentials.split(':')
        except (ValueError, TypeError):
            return None

        # Use the email address as the username
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None

        # Authenticate the user using the provided password
        if user.check_password(password):
            return (user, None)

        return None
