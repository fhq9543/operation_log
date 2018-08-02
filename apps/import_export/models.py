from django.db import models

# Create your models here.
class ImportRecord(models.Model):
    """导入操作记录表"""
    file_name = models.CharField(
        max_length=100, verbose_name='文件名称', help_text='文件名称')
    status = models.CharField(
        max_length=20, verbose_name='状态', help_text='状态')
    success_count = models.IntegerField(
        verbose_name='上传成功条数', help_text='上传成功条数')
    failed_count = models.IntegerField(
        default=0, verbose_name='上传失败条数', help_text='上传失败条数')
    operator = models.IntegerField(
        default=0, verbose_name='创建人', help_text='创建人')
    operator_name = models.CharField(
        max_length=100, verbose_name='创建人用户名', help_text='创建人用户名')
    file_url = models.URLField(
        blank=True, null=True, max_length=1000, verbose_name='文件url', help_text='文件url')
    extras = models.CharField(
        blank=True, null=True, max_length=500, verbose_name='其他参数', help_text='其他参数')
    create_time = models.DateTimeField(auto_now_add=True)


class ExportRecord(models.Model):
    """导出操作记录表"""
    file_name = models.CharField(
        max_length=100, verbose_name='文件名称', help_text='文件名称')
    status = models.CharField(
        max_length=20, verbose_name='状态', help_text='状态')
    operator = models.IntegerField(
        default=0, verbose_name='创建人', help_text='创建人')
    operator_name = models.CharField(
        max_length=100, verbose_name='创建人用户名', help_text='创建人用户名')
    download_url = models.URLField(
        max_length=1000, verbose_name='下载url', help_text='下载url')
    extras = models.CharField(
        blank=True, null=True, max_length=500, verbose_name='其他参数', help_text='其他参数')
    create_time = models.DateTimeField(auto_now_add=True)

