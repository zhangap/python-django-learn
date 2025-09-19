import time

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# AI_TIKTOK MOCK DATA
@csrf_exempt
def scan_ip(request):
    response = JsonResponse({
        'code': 200,
        'data': ['192.168.31.24', '192.168.31.108', '127.0.0.1'],
        'msg': '1111',
    })
    time.sleep(2)
    return response


@require_http_methods(['POST'])
@csrf_exempt
def check_index(request):
    response = JsonResponse({
        'code': 200,
        'data': [
            {
                'vid': 1,
                'state': 'running',
                'mac': '00:2b:25:29:80:ba',
                'ip': '192.168.31.24',
                'myt_ip': '192.168.31.24',
                'controller': '192.168.31.24',
                'mobileIp': '192.168.31.24',
                'index': 1,
            },
            {
                'vid': 2,
                'state': 'running',
                'mac': '00:2b:25:29:80:ba',
                'ip': '192.168.31.108',
                'myt_ip': '192.168.31.24',
                'controller': '192.168.31.24',
                'mobileIp': '192.168.31.108',
                'index': 2,
            }
        ],
        'msg': '1111',
    })
    time.sleep(2)
    return response


def myProcess(request):
    response = JsonResponse({
        'code': 200,
        'data': [],
        'msg': '1111',
    })
    time.sleep(1)
    return response
