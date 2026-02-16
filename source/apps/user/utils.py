import random
from django.utils import timezone
from datetime import timedelta
from .models import PhoneOTP


def generate_otp(phone):
    code = str(random.randint(100000, 999999))

    PhoneOTP.objects.create(
        phone_number=phone,
        code=code,
        expires_at=timezone.now() + timedelta(minutes=3)
    )

    return code