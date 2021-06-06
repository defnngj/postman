import json
import requests
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index(request):
    """
    默认页面
    """
    return render(request, "postman.html")


def send(request):
    """
    发送http请求
    """
    if request.method == "POST":
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        par_type = request.POST.get("par_type", "")
        par_value = request.POST.get("par_value", "")

        # str to dict
        header_dict = json.loads(header)
        par_value_dict = json.loads(par_value)

        if method == "get":
            r = requests.get(url, params=par_value_dict, headers=header_dict)
            return JsonResponse({"code": 10200, "message": "success", "data": r.text})

        elif method == "post":
            if par_type == "form":
                r = requests.post(url, data=par_value_dict, headers=header_dict)
                return JsonResponse({"code": 10200, "message": "success", "data": r.text})
            elif par_type == "json":
                r = requests.post(url, json=par_value_dict, headers=header_dict)
                return JsonResponse({"code": 10200, "message": "success", "data": r.text})
            else:
                return JsonResponse({"code": 10102, "message": "par type error", "data": ""})
        else:
            return JsonResponse({"code": 10101, "message": "no method", "data": ""})

    else:
        return JsonResponse({"code": 10100, "message": "request method error", "data": ""})
