from django.conf import settings
from rest_framework import request

from utils.http_request import send_request

OPERATION_API = settings.OPERATION_HOST + '/operation_log'


class OperationUserModule(tuple):
    """用户模块"""
    Customer = 'customer'
    Supplier = 'supplier'
    Supplier_Contract = 'supplier_contract'
    Supplier_Permission = 'supplier_permission'
    Operation = 'operation'
    Operation_Department = 'operation_department'
    Operation_Position = 'operation_position'
    Operation_Permission = 'operation_permission'
    Operation_Group = 'operation_group'


class OperationProductModule(tuple):
    """产品模块"""
    Product = 'product'
    Product_Brand = 'product_brand'
    Product_Category = 'product_category'
    Product_Model = 'product_model'
    Goods = 'goods'


class OperationOrderModule(tuple):
    pass


class OperationFinanceModule(tuple):
    pass


class OperationSlnModule(tuple):
    pass


class OperationPlatform(tuple):
    """操作平台"""
    Operation = 'operation'
    Supplier = 'supplier'
    Customer = 'customer'


class OperationActionFlag(tuple):
    """操作类型"""
    Add = 1
    Change = 2
    Delete = 3
    Audit = 4

    Active = 101  # 账号启用禁用
    Change_Password = 102  # 修改密码

    Authorizate = 201  # 产品授权
    Publish = 202  # 商品上下架


def create_operation_log(module, object_id, action_flag, platform, user, change_message, remark=None, extras=None):
    """
    创建操作日志
    :param module: 操作模块
    :param object_id: 对象id
    :param action_flag:  操作类型
    :param platform: 操作平台
    :param user: 操作用户
    :param change_message: 日志信息
    :param remark: 备注
    :param extras: 补充信息 json格式
    :return:
    """
    data = {
        'module': module,
        'key': object_id,
        'action_flag': action_flag,
        'platform': platform,
        'operator': user.id,
        'operator_name': user.username,
        'change_message': change_message,
        'remark': remark,
        'extras': extras
    }
    is_success, _ = send_request(OPERATION_API, None, 'POST', data=data)
    return is_success


if __name__ == '__main__':
    """
    使用示例
    1.操作模块: 分为五大模块，用户、产品、订单、财务、方案，具体模块名称按照相应前缀要求进行定义
    2.操作类型action_flag: 除公共定义的 增、删、改、审核 外，其他模块需自定义，如：用户模块以1xx定义，产品模块以2xx定义
    3.操作平台: 分三大平台，运营、供应商、客户
    4.对象id: 使用操作对象的主键
    """
    create_operation_log(
        OperationProductModule.Product,  # 模块名称
        'id',  # 操作对象主键id
        OperationActionFlag.Add,
        OperationPlatform.Operation,
        request.user,
        '新增产品')
