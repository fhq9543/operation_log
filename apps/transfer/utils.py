from apps.order.utils import order_record_get, order_record_post
from apps.user.utils import user_record_get, user_record_post
from apps.product.utils import product_record_get, product_record_post
from apps.finance.utils import finance_record_get, finance_record_post
from apps.sln.utils import sln_record_get, sln_record_post
from utils.response import res_code
from utils.http import APIResponse

from .common import OrderModuleList, FinanceModuleList, UserModuleList, ProductModuleList, SlnModuleList


def switch_get(module, request):
    if module in OrderModuleList:
        data = order_record_get(request)
    elif module in UserModuleList:
        data = user_record_get(request)
    elif module in ProductModuleList:
        data = product_record_get(request)
    elif module in FinanceModuleList:
        data = finance_record_get(request)
    elif module in SlnModuleList:
        data = sln_record_get(request)

    data = 'Need a parameter of module.'

    return APIResponse(rescode=res_code['error'], data=data)


def switch_post(module, data):
    if module in OrderModuleList:
        return order_record_post(data)
    elif module in UserModuleList:
        return user_record_post(data)
    elif module in ProductModuleList:
        return product_record_post(data)
    elif module in FinanceModuleList:
        return finance_record_post(data)
    elif module in SlnModuleList:
        return sln_record_post(data)
    else:
        return 'Mudule not found!', res_code['error']
