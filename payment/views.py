from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.http import HttpResponse
import json
import requests

# Create your views here.


amount = 1000 
description = "castilla.ir"
phone = '09023241014'
email = 'palahangmohammadbagher@gmail.com'
callbackURL = 'http://127.0.0.1:8080/'

def orderPayVerify(request):
    data = {
        'MerchantID': settings.MERCHANT,
        'Amount': amount,
        'CallbackURL': callbackURL,
        'Description': description,
        "Mobile": phone,
        "Email": email,
    }

    data = json.dumps(data)
    headers = {'content-type' : 'application/json', 'accept' : 'application/json'}
    res = requests.post(settings.ZP_API_REQUEST, data=data, headers=headers)
    
    if res.status_code == 200:
        response = res.json()
        if response['Status'] == 100:
            url = f"{settings.ZP_API_STARTPAY}{response['Authority']}"
            return redirect(url)
    else:
        return HttpResponse(str(res.json()['errors']))

class OrderPayView(View):
    def get(self, request):
        data = {
            'MerchantID' : settings.MERCHANT,
            'Amount' : amount,
            'CallbackURL' : callbackURL,
            'Description' : description,
              "metadata": {
                "mobile": phone,
                "email": email
            }
        }
    
        data = json.dumps(data)
        headers = {'content-type' : 'application/json', 'accept' : 'application/json'}
        res = requests.post(settings.ZP_API_REQUEST, data=data, headers=headers)

        if res.status_code == 200:
            response = res.json()
            print(response)
            if response['Status'] == 100:
                url = f"{settings.ZP_API_STARTPAY}{response['Authority']}"
                return redirect(url)
        else:
            return HttpResponse(str(res.json()['errors']))