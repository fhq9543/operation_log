import json

OrderModuleList = (
    'order',     # 订单
)

UserModuleList = (
    'customer',     # 采购企业
    'supplier',     # 供应商
    'operation',    # 运营
)

ProductModuleList = (
    'product',      # 产品
    'goods',        # 商品
)

FinanceModuleList = (
    'finance',      # 财务
)

SlnModuleList = (
    'sln',     # 方案
)


def check_json_format(raw_msg):
    """
    用于判断一个字符串是否符合Json格式
    :param self:
    :return:
    """
    if isinstance(raw_msg, str):    # 首先判断变量是否为字符串
        try:
            json.loads(raw_msg, encoding='utf-8')
        except ValueError:
            return False
        return True
    else:
        return False
