from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RestaurantUser, PhoneOTP
from .serializers import CreateUserSerializer
import requests

import random


class ValidatePhoneSendOTP(APIView):

    def post(self, request, *args, **kwargs):

        phone_number = request.data.get('phone')
        if phone_number:
            phone = str(phone_number)
            user = RestaurantUser.objects.filter(phone__exact=phone)
            if user.exists():
                return Response({
                    'status': False,
                    'detail': 'Phone Number is already exist'
                })
            else:
                key = send_otp(phone)
                if key:
                    old = PhoneOTP.objects.filter(phone__exact=phone)
                    if old.exists():
                        old = old.first()
                        count = old.count
                        if count > 10:
                            return Response({
                                'status': False,
                                'detail': 'Sending otp error. Limit Exceeded. Contact to Costumer Care'
                            })
                        old.count = count + 1
                        old.save()
                        print("Count increase ", count)
                        return Response({
                            'status': True,
                            'detail': 'OTP is sent successfully',
                        })
                    else:
                        PhoneOTP.objects.create(
                            phone=phone,
                            otp=key,

                        )
                        return Response({
                            'status': True,
                            'detail': 'OTP is sent successfully',
                        })

                else:
                    return Response({
                        'status': False,
                        'detail': 'Sending OTP Error'
                    })

        else:
            return Response({'status': False,
                             'detail': 'Phone Number is not given'})


class ValidateOTP(APIView):

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone', False)
        otp_sent = request.data.get('otp', False)

        if phone and otp_sent:
            old = PhoneOTP.objects.filter(phone__exact=phone)
            if old.exists():
                old = old.first()
                otp = old.otp
                if str(otp_sent) == str(otp):
                    old.validated = True
                    old.save()
                    return Response({
                        'status': True,
                        'detail': 'OTP Matched'
                    })
                else:
                    return Response({
                        'status': False,
                        'detail': 'OTP Incorrect'
                    })
            else:
                return Response({
                    'status': False,
                    'detail': 'First proceed via Send OTP  '
                })
        else:
            return Response({
                'status': False,
                'detail': 'Please provide both phone number and OTP for validate'
            })


class Register(APIView):
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone', False)

        if phone:
            old = PhoneOTP.objects.filter(phone__exact=phone)
            if old.exists():
                old = old.first()
                validated = old.validated

                if validated:
                    temp_data = {
                        'phone': phone
                    }
                    serializer = CreateUserSerializer(data=temp_data)
                    serializer.is_valid(raise_exception=True)
                    user = serializer.save()
                    old.delete()
                    return Response({
                        'status': True,
                        'detail': 'Account Created'
                    })
                else:
                    return Response({
                        'status': False,
                        'detail': "OTP haven't verified yet"
                    })
            else:
                return Response({
                    'status': False,
                    'detail': 'Please verify phone number first'
                })

        else:
            return Response({
                'status': False,
                'detail': 'Phone number is not available'
            })


def send_otp(phone):
    if phone:
        key = random.randint(999, 9999)
        phone = str(phone)
        link = f"https://www.txtguru.in/imobile/api.php?username=moozyindia88&password=28071997&source=MMOOZY&dmobile={phone}&dltentityid=1501340370000027813&dltheaderid=1505162194143833887&dlttempid=1507162194517361989&message={key} is OTP to proceed.Moozy Karo Mauj Karo - MOOZY"
        result = requests.get(link, verify=False)
        print(key)
        return key
    else:
        return False




