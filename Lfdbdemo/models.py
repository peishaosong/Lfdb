from django.db import models

from django.db import transaction
# Create your models here.
class chang(models.Model):
    name = models.CharField(max_length=200,verbose_name='厂名', null=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')



    class Meta:
        verbose_name = "厂别"
        verbose_name_plural = "厂别管理"

    def __str__(self):
        return self.name


class bumen(models.Model):
    bumen = models.CharField(max_length=200, verbose_name='部门', null=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', null=True)
    chang = models.ForeignKey(chang, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='厂别')

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门管理"

    def __str__(self):
        return self.bumen


class title(models.Model):
    name = models.CharField(max_length=128,verbose_name='岗位', null=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', null=True)
    chang = models.ForeignKey(chang, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='厂别')
    bumen = models.ForeignKey(bumen, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='部门')

    class Meta:
        verbose_name = '岗位'
        verbose_name_plural = '岗位管理'

    def __str__(self):
        return self.name


class person(models.Model):
    name = models.CharField(max_length=128, verbose_name='姓名', help_text='员工的名字', null=False, blank=False,
                            db_index=True)
    useid = models.IntegerField(max_length=128, verbose_name='工号', null=True)
    gender_choices = (
        (0, '未知'),
        (1, '男'),
        (2, '女'),
    )
    zh_choices =(
        (0, '离职'),
        (1, '在职'),
        (2, '停职')
    )
    hy_choices =(
        (0, '未知'),
        (1, '未婚'),
        (2, '已婚'),
    )
    xl_choices = (
        (0, '初中及以下'),
        (1, '高中/中专'),
        (2, '大专'),
        (3, '本科及以上'),
    )
    gender = models.IntegerField(choices=gender_choices, verbose_name='性别', default=0)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='创建时间',null=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True, null= True)
    chang = models.ForeignKey(chang, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='厂别')
    bumen = models.ForeignKey(bumen, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='部门')
    title = models.ForeignKey(title, on_delete=models.SET_NULL, blank=False,  null=True, verbose_name='岗位')
    number = models.CharField(max_length=18, verbose_name='身份证号码', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='手机号')
    birthday = models.DateField(verbose_name='生日')
    age = models.IntegerField(verbose_name='年龄',)
    address = models.TextField(verbose_name='家庭住址')
    date = models.DateField(verbose_name='入职日期')
    zhuangtai = models.IntegerField(choices=zh_choices, verbose_name='状态', default=1)
    mingzu = models.CharField(max_length=18, verbose_name='民族')
    hunyin = models.IntegerField(choices=hy_choices, verbose_name='婚姻状态', default=0)
    xueli = models.IntegerField(choices=xl_choices, verbose_name='学历水平', default=1)
    shebao = models.DateField(verbose_name='社保购买日期')
    beizhu = models.TextField(verbose_name='备注', help_text='可填写过往工作经历及岗位', null=True)
    cardnumber = models.CharField(max_length=30, verbose_name='银行卡号', null=True)
    shengshi = models.CharField(max_length=50, verbose_name='银行卡所属地', null=True)
    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工管理'



    def __str__(self):
        return self.name




