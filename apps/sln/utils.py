from .models import SlnRecord
from .serializers import SlnRecordSerializer
from utils.response import res_code
from utils.http import get_limit, APIResponse, CONTENT_RANGE, CONTENT_TOTAL
from utils.string_extension import safe_int
import json
import time
from apps.transfer.common import check_json_format


def sln_record_get(request):
    logs = SlnRecord.objects.all()
    offset = safe_int(request.query_params.get('offset', 0))
    limit = safe_int(request.query_params.get('limit', 15))
    limit = get_limit(limit)

    module = request.query_params.get('module')
    action_flag = request.query_params.get('action_flag')
    key = request.query_params.get('key')
    platform = request.query_params.get('platform')
    start_time = request.query_params.get('start_time')
    end_time = request.query_params.get('end_time')

    if module:
        logs = logs.filter(module=module)
    if key:
        logs = logs.filter(key=key)
    if platform:
        logs = logs.filter(platform=platform)
    if action_flag:
        logs = logs.filter(action_flag=action_flag)
    if start_time and end_time:
        start_time += ' 00:00:00'
        end_time += ' 23:59:59'
        logs = logs.filter(create_time__gte=start_time).filter(create_time__lte=end_time)

    total = logs.count()
    logs = logs.order_by('-create_time')[offset:offset + limit]

    serializer = SlnRecordSerializer(logs, many=True)

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


def sln_record_post(data):
    # 如果extras是json就转str存入数据库
    if 'extras' in data.keys():
        if isinstance(data['extras'], dict):
            data['extras'] = json.dumps(data['extras'])

    serializer = SlnRecordSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, res_code['success']
    return serializer.errors, res_code['error']
