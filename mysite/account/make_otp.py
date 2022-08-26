# tanzimate marbud b kar ba kave negar + tabe ijade adade random baraye verify kardan:
# -----------------------------------------------------------------------------------------
from kavenegar import *
from random import randint


def send_otp(mobile, otp):

    # shomare mobile bayad array bashe:
    mobile = [mobile, ]

    try:
        api = KavenegarAPI('426878736650367675466E4F4E51554E5258656C734C644F4C6D7A715674357A4839575757436C386B6C493D')

        params = {'sender': '100047778', 'receptor': mobile, 'message': 'Your OTP  {}'.format(otp)}

        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


def get_random_otp():
    return randint(1000, 9999)
