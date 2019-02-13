from rest_framework.views import APIView
from utils.response import res_code
from utils.http import get_limit, APIResponse, CONTENT_RANGE, CONTENT_TOTAL
from utils.string_extension import safe_int
import json
import time
from apps.transfer.common import check_json_format

from .models import ImportRecord, ExportRecord
from .serializers import ImportRecordSerializer, ExportRecordSerializer


class ImportView(APIView):
    def get(self, request):
        logs = ImportRecord.objects.all()
        offset = safe_int(request.query_params.get('offset', 0))
        limit = safe_int(request.query_params.get('limit', 15))
        limit = get_limit(limit)

        file_name = request.query_params.get('file_name')
        status = request.query_params.get('status')
        operator_name = request.query_params.get('operator_name')
        start_time = request.query_params.get('start_time')
        end_time = request.query_params.get('end_time')

        if file_name:
            logs = logs.filter(file_name=file_name)
        if status:
            logs = logs.filter(status=status)
        if operator_name:
            logs = logs.filter(operator_name=operator_name)
        if start_time and end_time:
            start_time += ' 00:00:00'
            end_time += ' 23:59:59'
            logs = logs.filter(create_time__gte=start_time).filter(create_time__lte=end_time)

        total = logs.count()
        logs = logs.order_by('-create_time')[offset:offset + limit]

        serializer = ImportRecordSerializer(logs, many=True)

        # extras转为dict
        for data in serializer.data:
            if check_json_format(data['extras']):
                data['extras'] = json.loads(data['extras'])
            data['create_time'] = time.mktime(time.strptime(data['create_time'], '%Y-%m-%dT%H:%M:%S.%f'))

        response = APIResponse(success=True, data=serializer.data)
        # 分页数据
        response[CONTENT_RANGE] = '{0}-{1}'.format(offset, offset + len(logs))
        response[CONTENT_TOTAL] = total
        return response

    def post(self, request):
        # 如果extras是json就转str存入数据库
        if 'extras' in request.data.keys():
            if isinstance(request.data['extras'], dict):
                request.data['extras'] = json.dumps(request.data['extras'])

        serializer = ImportRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse(rescode=res_code['success'], data=serializer.data)
        return APIResponse(rescode=res_code['error'], data=serializer.errors)


class ExportView(APIView):
    def get(self, request):
        logs = ExportRecord.objects.all()
        offset = safe_int(request.query_params.get('offset', 0))
        limit = safe_int(request.query_params.get('limit', 15))
        limit = get_limit(limit)

        file_name = request.query_params.get('file_name')
        status = request.query_params.get('status')
        operator_name = request.query_params.get('operator_name')
        start_time = request.query_params.get('start_time')
        end_time = request.query_params.get('end_time')

        if file_name:
            logs = logs.filter(file_name=file_name)
        if status:
            logs = logs.filter(status=status)
        if operator_name:
            logs = logs.filter(operator_name=operator_name)
        if start_time and end_time:
            start_time += ' 00:00:00'
            end_time += ' 23:59:59'
            logs = logs.filter(create_time__gte=start_time).filter(create_time__lte=end_time)

        total = logs.count()
        logs = logs.order_by('-create_time')[offset:offset + limit]

        serializer = ExportRecordSerializer(logs, many=True)

        # extras转为dict
        for data in serializer.data:
            if check_json_format(data['extras']):
                data['extras'] = json.loads(data['extras'])
            data['create_time'] = time.mktime(time.strptime(data['create_time'], '%Y-%m-%dT%H:%M:%S.%f'))

        response = APIResponse(success=True, data=serializer.data)
        # 分页数据
        response[CONTENT_RANGE] = '{0}-{1}'.format(offset, offset + len(logs))
        response[CONTENT_TOTAL] = total
        return response

    def post(self, request):
        # 如果extras是json就转str存入数据库
        if 'extras' in request.data.keys():
            if isinstance(request.data['extras'], dict):
                request.data['extras'] = json.dumps(request.data['extras'])

        serializer = ExportRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse(rescode=res_code['success'], data=serializer.data)
        return APIResponse(rescode=res_code['error'], data=serializer.errors)

