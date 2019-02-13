
from __future__ import absolute_import
from rest_framework.views import APIView

from operation_log.settings import RUN_MODE
from .utils import switch_get, switch_post

from utils.http import APIResponse
from utils.response import res_code
from celery import shared_task


@shared_task
def test_post(data):
    try:
        module = data['module']
    except Exception as e:
        data = 'Need input a parameter of module.'
        return APIResponse(rescode=res_code['error'], data=data)
    module_prefix = module.split('_')[0]
    data, status = switch_post(module_prefix, data)
    return data, status


@shared_task
def proc_post(data):
    try:
        module = data['module']
    except Exception as e:
        data = 'Need input a parameter of module.'
        return APIResponse(rescode=res_code['error'], data=data)
    module_prefix = module.split('_')[0]
    data, status = switch_post(module_prefix, data)
    return data, status


class RecordList(APIView):
    def get(self, request):
        module = request.query_params.get('module')
        if module:
            module_prefix = module.split('_')[0]
            response = switch_get(module_prefix, request)
        else:
            data = 'Need a parameter of module.'
            return APIResponse(rescode=res_code['error'], data=data)
        return response

    def post(self, request):
        if RUN_MODE == "PRODUCT":
            proc_post.delay(request.data)
        else:
            test_post.delay(request.data)
        return APIResponse(success=True)
