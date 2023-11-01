import requests
import json
import base64


class Pay:
    
    def __init__(self):
        pass

    def send_login(self):
        r = requests.post(
            url="https://payme.uz/api/users.check_phone",
            headers={
                "accept":"application/json, text/plain, */*",
                "accept-encoding":"gzip, deflate, br",
                "accept-language":"en-US,en;q=0.9",
                "adrum":"isAjax:true",
                "app-version":"2.40",
                "connection":"keep-alive",
                "content-type":"application/json; charset=UTF-8",
                "cookie":"cookiesession1=678A3E1011DCDF8FF6EFEFDA6DD1A873; ngx-device=d0ea2dc7bb12c8a12e2318c67599bd853f67138826864e82db0296fee3fdde05; _ga=GA1.1.329187090.1693272563; _ym_uid=169327256323256885; _ym_d=1693272563; _fbp=fb.1.1693272566090.382785881; _ym_isad=1; _ym_visorc=b; _ga_W9V4BPZNLX=GS1.1.1693272562.1.1.1693272574.48.0.0; _ga_PFZ4HL7H2T=GS1.1.1693272562.1.1.1693272574.0.0.0",
                "referer":'https"://payme.uz/login',
                "sec-ch-ua":'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
                "sec-ch-ua-mobile":"?0",
                "host":"payme.uz",
                "origin":"https://payme.uz",
                "sec-ch-ua-platform":'"Windows"',
                # "content-length":"61",
                "sec-fetch-dest":'empty',
                "sec-fetch-mode":'cors',
                "sec-fetch-site":'same-origin',
                "track-id":'d0ea2dc7bb12c8a12e2318c67599bd853f67138826864e82db0296fee3fdde05',
                "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                "x-accept-language":"ru"
            },
            data=json.dumps({
                "method": "users.check_phone",
                "params": {
                    "phone": "905650213"
                }
            })
        )
        return r

    def valid_login(self):        
        r = requests.post(
            url="https://payme.uz/api/users.log_in",
            headers={
                "accept":"application/json, text/plain, */*",
                "accept-encoding":"gzip, deflate, br",
                "accept-language":"en-US,en;q=0.9",
                "adrum":"isAjax:true",
                "app-version":"2.40",
                "connection":"keep-alive",
                "content-type":"application/json; charset=UTF-8",
                "cookie":"cookiesession1=678A3E1011DCDF8FF6EFEFDA6DD1A873; ngx-device=d0ea2dc7bb12c8a12e2318c67599bd853f67138826864e82db0296fee3fdde05; _ga=GA1.1.329187090.1693272563; _ym_uid=169327256323256885; _ym_d=1693272563; _fbp=fb.1.1693272566090.382785881; _ym_isad=1; _ym_visorc=b; _ga_W9V4BPZNLX=GS1.1.1693272562.1.1.1693272574.48.0.0; _ga_PFZ4HL7H2T=GS1.1.1693272562.1.1.1693272574.0.0.0",
                "referer":'https"://payme.uz/login',
                "sec-ch-ua":'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
                "sec-ch-ua-mobile":"?0",
                "host":"payme.uz",
                "origin":"https://payme.uz",
                "sec-ch-ua-platform":'"Windows"',
                "sec-fetch-dest":'empty',
                "sec-fetch-mode":'cors',
                "sec-fetch-site":'same-origin',
                "track-id":'d0ea2dc7bb12c8a12e2318c67599bd853f67138826864e82db0296fee3fdde05',
                "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                "x-accept-language":"ru"
            },
            data=json.dumps({
                "method": "users.log_in",
                "params": {
                    "login": "905650213",
                    "password": "UZBcoders2005"
                }
            })
        )
        return r

sendsms = Pay().send_sms()

print(sendsms)
print(sendsms.text)