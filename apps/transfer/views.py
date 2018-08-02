from rest_framework.views import APIView
from .utils import switch_get, switch_post

from utils.http import APIResponse


class RecordList(APIView):
    def get(self, request):
        module = request.query_params.get('module')
        response = switch_get(module, request)
        return response

    def post(self, request):
        module = request.data['module']
        data, status = switch_post(module, request.data)
        return APIResponse(rescode=status, data=data)
