# Generated by Django 2.0.7 on 2018-08-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(help_text='操作模块', max_length=20, verbose_name='操作模块')),
                ('key', models.CharField(help_text='操作对象ID', max_length=30, verbose_name='操作对象ID')),
                ('action_flag', models.IntegerField(help_text='操作类型', verbose_name='操作类型')),
                ('operator', models.IntegerField(default=0, help_text='操作员', verbose_name='操作员')),
                ('operator_name', models.CharField(blank=True, help_text='操作员用户名', max_length=30, null=True, verbose_name='操作员用户名')),
                ('platform', models.CharField(help_text='操作平台', max_length=20, verbose_name='操作平台')),
                ('change_message', models.CharField(help_text='操作信息', max_length=500, verbose_name='操作信息')),
                ('remark', models.CharField(blank=True, help_text='备注', max_length=30, null=True, verbose_name='备注')),
                ('extras', models.CharField(blank=True, help_text='其他参数', max_length=500, null=True, verbose_name='其他参数')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
