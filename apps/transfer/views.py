from rest_framework.views import APIView
from .utils import switch_get, switch_post

from utils.http import APIResponse


class RecordList(APIView):
    def get(self, request):
        module = request.query_params.get('module')
        if module:
            module_prefix = module.split('_')[0]
        response = switch_get(module_prefix, request)
        return response

    def post(self, request):
        module = request.data['module']
        if module:
            module_prefix = module.split('_')[0]
        data, status = switch_post(module_prefix, request.data)
        return APIResponse(rescode=status, data=data)
