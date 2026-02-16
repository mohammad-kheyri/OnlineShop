import requests
from base import settings

def normalize_phone(phone):
    phone = phone.strip()

    if phone.startswith("+"):
        phone = phone[1:]

    if phone.startswith("0"):
        phone = "98" + phone[1:]

    return phone

def send_sms(phone, message):
    phone = normalize_phone(phone)
    url = f"https://api.kavenegar.com/v1/{settings.KAVENEGAR_API_KEY}/sms/send.json"

    payload = {
        "receptor": phone,          # receiver phone
        "sender": settings.KAVENEGAR_SENDER,
        "message": message,
    }

    try:
        response = requests.post(url, data=payload)
        data = response.json()

        if response.status_code == 200 and data["return"]["status"] == 200:
            return True
        else:
            print("Kavenegar Error:", data)
            return False

    except Exception as e:
        print("SMS Exception:", str(e))
        return False
    



