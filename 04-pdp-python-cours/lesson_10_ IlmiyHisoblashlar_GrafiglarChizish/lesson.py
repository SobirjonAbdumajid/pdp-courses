# # import turtle

# # keith = turtle.Turtle()
# # keith.speed(1)
# # keith.forward(100)
# # keith.left(90)
# # keith.forward(100)
# # keith.left(90)
# # keith.forward(100)
# # keith.left(90)
# # keith.forward(100)
# # keith.left(90)
# # turtle.done()


# import random
# import string

# def generate_code_token(length=32):
#     code_token = ''.join(random.choice(string.ascii_letters) for i in range(length))

#     return code_token



# print(generate_code_token())

import uuid
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from twilio.base.exceptions import TwilioRestException

from .models import CustomUser, CodeConfirmation
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.hashers import make_password
from django.conf import settings
from twilio.rest import Client

from .serializers import UserSerializer


def generate_token(length=32):
    return str(uuid.uuid4()).replace("-", "")


def generate_code(length=4):
    import random
    numbers = "0123456789"
    return "".join(random.choice(numbers) for _ in range(length))


def send_sms(phone_number, message):
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        print("SMS sent successfully:", message.sid)
    except TwilioRestException as e:
        print(f"Error sending SMS: {e}")


class RegisterApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        phone = request.data.get('phone')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        ex_user = CustomUser.objects.filter(phone=phone).first()
        if ex_user:
            return Response({'massage': 'Bu raqam tizimda mavjud'})
        user = CustomUser.objects.create_user(
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            password=make_password(password),
            is_active=True
        )
        return Response({
            'user': UserSerializer(user).data,
            'massage': 'Register Successful!',
        })


class LoginStartApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        phone = request.data.get('phone')
        if not phone:
            return Response({'error': 'Phone number is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(phone=phone)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        sms_code = generate_code()
        code_token = generate_token()  # Generate 32-character token

        CodeConfirmation.objects.update_or_create(
            user=user, defaults={'code': sms_code, 'code_token': code_token}
        )

        send_sms(phone, f'Your verification code is: {sms_code}')
        return Response({'code_token': code_token})


class LoginEndApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        code_token = request.data.get('code_token')
        sms_code = request.data.get('sms_code')

        try:
            # Check for valid token first
            confirmation = CodeConfirmation.objects.get(code_token=code_token, code=sms_code)
            user = confirmation.user
        except (CodeConfirmation.DoesNotExist, TokenError):
            return Response({'error': 'Invalid code or code_token.'}, status=status.HTTP_400_BAD_REQUEST)

        CodeConfirmation.objects.filter(user=user).delete()  # Invalidate code after use

        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'Login successful.',
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        })