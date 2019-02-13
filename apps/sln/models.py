from django.db import models


class SlnRecord(models.Model):
    """方案模块操作记录表"""
    module = models.CharField(
        max_length=20, verbose_name='操作模块', help_text='操作模块')
    key = models.CharField(
        max_length=30, verbose_name='操作对象ID', help_text='操作对象ID')
    action_flag = models.IntegerField(
        verbose_name='操作类型', help_text='操作类型')
    operator = models.IntegerField(
        default=0, verbose_name='操作员', help_text='操作员')
    operator_name = models.CharField(
        blank=True, null=True, max_length=30, verbose_name='操作员用户名', help_text='操作员用户名')
    platform = models.CharField(
        max_length=20, verbose_name='操作平台', help_text='操作平台')
    change_message = models.CharField(
        max_length=500, verbose_name='操作信息', help_text='操作信息')
    remark = models.CharField(
        blank=True, null=True, max_length=30, verbose_name='备注', help_text='备注')
    extras = models.CharField(
        blank=True, null=True, max_length=500, verbose_name='其他参数', help_text='其他参数')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sln_records'
