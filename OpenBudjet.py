import requests
import json
from dotenv import load_dotenv
import os
import base64

load_dotenv()

class OpenBudjet:
    def __init__(self):
        self.initiativeId = os.getenv("initiativeId")
        self.secretKey = os.getenv('secretKey')
        self.referer = os.getenv('referer')
        
    def getVoice(self) -> {
            "img":"base64 img",
            "captchaKey":"token img"
        }:
        r = requests.get(
            url="https://openbudget.uz/api/v2/vote/captcha-2",
            headers={
                "accept-encoding":"gzip",
                "access-captcha":"czM2ZTEzMms3MnIxMDhlNTV0",
                "host":"openbudget.uz",
                "referer":self.referer,
                "user-agent":"Dart/3.0 (dart:io)",
                "x-xsrf-token":"czM2ZTEzMms3MnIxMDhlNTV07989"
            }
        )
        
        if r.status_code != 200:
            return {
                "ok":False,
                "status-code":r.status_code
            }
        r = r.json()
        
        imgKey = r['captchaKey'][::-1]
        
        sample_string_bytes = imgKey.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        imgKeyBase64 = base64_bytes.decode("ascii")
        
        bugImg64 = r['image'].replace(imgKeyBase64,'')

        return {
            "img":bugImg64,
            "captchaKey":r['captchaKey'],
            "ok":True
        }
    
    def robotValid(self, **kwargs):
        r = requests.post(
            url="https://openbudget.uz/api/v2/vote/check",
            headers={
                "accept-encoding":"gzip",
                "content-length":"102",
                "content-type":"application/json; charset=utf-8",
                "cookie":"",
                "host":"openbudget.uz",
                "referer":self.referer,
                "user-agent":"Dart/3.0 (dart:io)",
                "x-xsrf-token":""
            },
            data=json.dumps({
                "captchaKey": kwargs['captchaKey'],
                "captchaResult": kwargs['robotResult'],
                "phoneNumber": "998{}".format(kwargs['phone']),
                "boardId": 31
            })
        )  
        return r
        
    def smsValid(self, **kwargs):
        r = requests.post(
            url="https://openbudget.uz/api/v2/vote/private-verify-mobile/ewaL7Js8LEM3EYvD",
            headers={
                "accept-encoding":"gzip",
                "content-length":"102",
                "content-type":"application/json; charset=utf-8",
                "cookie":"",
                "host":"openbudget.uz",
                "referer":self.referer,
                "user-agent":"Dart/3.0 (dart:io)",
                "x-xsrf-token":""
            },
            data=json.dumps({
                    "otpKey": kwargs['otpKey'],
                    "otpCode": kwargs['otpCode'],
                    "initiativeId": self.initiativeId,
                    "subinitiativesId": [],
                    "secretKey": self.secretKey
            })
        )  
        return r
        
# getVoice = OpenBudjet().getVoice()
# print(getVoice)
# robotResult=int(input("robot: "))
# robot = OpenBudjet().robotValid(
#     phone="905650213",
#     captchaKey=getVoice['captchaKey'],
#     robotResult=robotResult
#     ).json()

# sms_code = input("sms code: ")
# smsValid = OpenBudjet().smsValid(otpKey=robot['otpKey'], sms_code=sms_code)

# print(smsValid)
# print(smsValid.status_code)
# print(smsValid.text)