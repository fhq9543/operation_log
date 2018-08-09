from rest_framework.views import APIView
from .utils import switch_get, switch_post

from utils.http import APIResponse
from utils.response import res_code


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
        try:
            module = request.data['module']
        except Exception as e:
            data = 'Need input a parameter of module.'
            return APIResponse(rescode=res_code['error'], data=data)
        module_prefix = module.split('_')[0]
        data, status = switch_post(module_prefix, request.data)
        return APIResponse(rescode=status, data=data)
