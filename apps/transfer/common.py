import json

OrderModuleList = (
    'order_status',     # 订单状态
    'order_sales_return',     # 退货
    'order_after_sale'        # 售后
)

UserModuleList = (
    'customer_user',     # 采购企业用户
    'customer_info',     # 采购企业用户信息
    'customer_sub',     # 采购企业子账号

    'supplier_info',     # 供应商信息
    'supplier_audit',       # 供应商审核
    'supplier_contract',         # 供应商合同
    'supplier_permission',      # 供应商权限

    'operation_department',    # 运营部门
    'operation_user',           # 运营用户组
    'operation_position',             # 运营职位
    'operation_permission',     # 运营权限
    'operation_group',     # 运营分组权限
)

ProductModuleList = (
    'product',      # 产品
    'product_brand',        # 产品品牌
    'product_category',      # 产品目录

    'goods',        # 商品
    'goods_audit',      # 商品审核
    'goods_publish',    # 商品上下架
)

FinanceModuleList = (
    'finance_refund',      # 退款
    'finance_check',      # 对账单
    'finance_invoice',      # 发票
    'finance_settlement',      # 结算
)

SlnModuleList = (
    'Sln_quote',          # 方案询价
    'Sln_order',     # 方案订单
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