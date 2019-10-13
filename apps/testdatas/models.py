from datetime import datetime   #系统的包放在最上面

from django.db import models   #第二个级别的就是第三方包
from django.contrib.auth import  get_user_model  #导入get_user_model

from wanwenyc.settings import DJANGO_SERVER_YUMING

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值
# Create your models here.


class ClickAndBack(models.Model):#继承django的Model模块
    """
    点击滑动返回测试场景测试数据
    """
    test_project = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    test_module = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试模块")
    test_page = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    test_case_title = models.CharField(max_length=200, default="", verbose_name=u"测试内容的名称")
    is_run_case = models.BooleanField(default=True,verbose_name=u"是否运行")
    current_page_click_ele_find = models.CharField(max_length=100, default="xpath",
                                                    verbose_name=u"当前页面要点击元素查找风格",
                                                    help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                              u"link_text、partial_link_text、css_selector、xpath")
    current_page_click_ele_find_value = models.CharField(max_length=1000, default="",
                                                         verbose_name=u"当前页面要点击元素查找风格的确切值")
    is_new = models.BooleanField(default=False, verbose_name=u"是否新窗口")
    next_page_check_ele_find= models.CharField(max_length=100,
                                             default="xpath", verbose_name=u"下一页面标识元素查找风格",
                                             help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                       u"link_text、partial_link_text、css_selector、xpath")
    next_page_check_ele_find_value = models.CharField(max_length=1000, default="",
                                                         verbose_name=u"下一页面标识元素查找风格的确切值")
    case_counts = models.IntegerField(default="1",verbose_name="用例循环次数",help_text=u"用例循环次数，请填写数字，"
                                                                   u"例如：1、2、3")
    depend_case = models.ForeignKey('self', default="", null=True, blank=True,
                                   verbose_name=u"依赖的前置用例",on_delete=models.PROTECT)
    write_user = models.ForeignKey(User,related_name="writeuser",null=True, blank=True,
                                   verbose_name=u"添加用例人", on_delete=models.PROTECT)

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"点击场景"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.test_case_title

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testdatas/clickandbackcopy/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加"   #为go_to函数名个名字







class NewAddAndCheck(models.Model):#继承django的Model模块
    """
    新增数据场景
    """
    test_project = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    test_module = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试模块")
    test_page = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    case_priority = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("P0", u"冒烟用例"), ("P1", u"系统的重要功能用例") , ("P2", u"系统的一般功能用例"), ("P3", "极低级别的用例")),
                                     default="P1",
                                     verbose_name=u"用例优先级")
    test_case_title = models.CharField(max_length=200, default="", verbose_name=u"测试内容的名称")
    is_run_case = models.BooleanField(default=True,verbose_name=u"是否运行")
    depend_click_case = models.ForeignKey(ClickAndBack, default="", null=True, blank=True,
                                   verbose_name=u"依赖的点击场景的用例",on_delete=models.PROTECT)



    confirm_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                        verbose_name=u"确定按钮查找风格",
                                        help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                  u"link_text、partial_link_text、css_selector、xpath")
    confirm_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"确定按钮查找风格的确切值")
    is_click_cancel = models.BooleanField(default=False,verbose_name=u"是否点击取消按钮")
    cancel_ele_find = models.CharField(max_length=100, default="xpath", null=True, blank=True,
                                       verbose_name=u"取消按钮查找风格",
                                       help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                 u"link_text、partial_link_text、css_selector、xpath")
    cancel_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"取消按钮查找风格的确切值")
    is_submit_success = models.BooleanField(default=True,verbose_name=u"是否添加成功")

    is_signel_page = models.BooleanField(default=False, verbose_name=u"是否单页面")

    page_number_xpath = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"页数层xpath路径值")

    result_table_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                             verbose_name=u"结果表格查找风格",
                                             help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                       u"link_text、partial_link_text、css_selector、xpath")
    result_table_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"结果表格查找风格的确切值")
    table_colnum_counts = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"结果表格总列数",help_text=u"结果表格总列数，请填写数字，"
                                                        u"例如：1、2、3")
    case_counts = models.IntegerField(default="1",verbose_name="循环次数",help_text=u"循环次数，请填写数字，"
                                                                   u"例如：1、2、3")
    write_user = models.ForeignKey(User,null=True, blank=True,verbose_name=u"添加人", on_delete=models.PROTECT)

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"新增场景"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.test_case_title

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testdatas/newaddandcheckcopy/{}/'>复制新加不带关联</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加不带关联"   #为go_to函数名个名字

    def go_to_with_relevance(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testdatas/newaddandcheckcopywithrelevance/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to_with_relevance.short_description = u"复制新加"   #为go_to函数名个名字




class InputTapInputText(models.Model):
    """
    新增数据场景依赖的文本输入框模型
    """
    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)

    input_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"输入框查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    input_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"输入框查找风格的确切值")
    is_auto_input = models.BooleanField(default=False, verbose_name=u"是否自动输入")
    auto_input_type = models.CharField(choices=(('1','数字'),('2','字母'),('3','数字和字母'),('4','数字和字母和特殊符号'),('5','数字和字母和特殊符号和转义字符'),('6','汉字')),
                                       null=True, blank=True,
                                       max_length=10,default='6',verbose_name="自动输入字符的类型")
    auto_input_long = models.CharField(max_length=100,default="300",null=True, blank=True,
                                          verbose_name="自动输入的字符的个数",help_text=u"字符的个数，请填写数字，"
                                                                   u"例如：1、2、3")

    input_text = models.CharField(max_length=300,default="",null=True, blank=True,
                                  verbose_name=u"输入框中要输入的内容")
    is_with_time = models.BooleanField(default=True,verbose_name=u"是否带时间串")
    is_check = models.BooleanField(default=True,verbose_name=u"是否进行验证")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"文本输入框相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.input_ele_find



class InputTapInputFile(models.Model):
    """
    新增数据场景依赖的文件输入框模型
    """
    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)

    input_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"输入框查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    input_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"输入框查找风格的确切值")
    input_file = models.CharField(max_length=300,default="",null=True, blank=True,
                                  verbose_name=u"输入框中要输入的文件路径",
                                  help_text = u"多个文件路径之间以半角逗号隔开,例如“D:\\timg.jpg,/root/timg.jpg”，会获取第一个有效路径")
    input_class_name = models.CharField(max_length=300,default="",null=True, blank=True,
                                        verbose_name=u"隐藏输入框的类名")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"文件输入框相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.input_ele_find_value


class InputTapInputDateTime(models.Model):
    """
    新增数据场景依赖的时间输入框模型
    """
    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)

    input_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"时间输入框查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    input_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"时间输入框查找风格的确切值")

    date_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"日期元素查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    date_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"日期元素查找风格的确切值")

    last_month_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"上一月按钮查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    last_month_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"上一月按钮查找风格的确切值")
    click_last_month_counts = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"点击上一月按钮的次数",help_text=u"点击上一月按钮的次数，请填写数字，"
                                                        u"例如：1、2、3")

    next_month_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"下一月按钮查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    next_month_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"下一月按钮查找风格的确切值")

    click_next_month_counts = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"点击下一月按钮的次数",help_text=u"点击下一月按钮的次数，请填写数字，"
                                                        u"例如：1、2、3")

    last_year_ele_find = models.CharField(max_length=100, default="xpath", null=True, blank=True,
                                           verbose_name=u"上一年按钮查找风格",
                                           help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                     u"link_text、partial_link_text、css_selector、xpath")
    last_year_ele_find_value = models.CharField(max_length=1000, default="", null=True, blank=True,
                                                 verbose_name=u"上一年按钮查找风格的确切值")
    click_last_year_counts = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"点击上一年按钮的次数",help_text=u"点击上一年按钮的次数，请填写数字，"
                                                        u"例如：1、2、3")

    next_year_ele_find = models.CharField(max_length=100, default="xpath", null=True, blank=True,
                                           verbose_name=u"下一年按钮查找风格",
                                           help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                     u"link_text、partial_link_text、css_selector、xpath")
    next_year_ele_find_value = models.CharField(max_length=1000, default="", null=True, blank=True,
                                                 verbose_name=u"下一年按钮查找风格的确切值")
    click_next_year_counts = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"点击下一年按钮的次数",help_text=u"点击下一年按钮的次数，请填写数字，"
                                                        u"例如：1、2、3")

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"时间输入框相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.input_ele_find_value


class RadioAndReelectionLabel(models.Model):
    """
    新增数据场景依赖的单选项和复选项模型
    """
    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)

    label_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"选项标签查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    label_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"选项标签查找风格的确切值")

    is_check = models.BooleanField(default=True,verbose_name=u"是否选中")
    checked_add_attribute = models.CharField(max_length=100, default="",null=True, blank=True,
                                         verbose_name=u"元素被选中后新增的属性")
    checked_add_attribute_value = models.CharField(max_length=100, default="",null=True, blank=True,
                                         verbose_name=u"元素被选中后新增的属性的值")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"单选项和复选项相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.label_ele_find_value


class SelectTapSelectOption(models.Model):
    """
    新增数据场景依赖的选项框模型
    """
    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)

    select_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                       verbose_name=u"选项框的查找风格",
                                       help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                 u"link_text、partial_link_text、css_selector、xpath")
    select_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"选项框查找风格的确切值")
    select_option_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                              verbose_name=u"选项的查找风格",
                                              help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                        u"link_text、partial_link_text、css_selector、xpath")
    select_option_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"选项查找风格的确切值")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"选项框相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.select_ele_find_value


class SelectTapSelectText(models.Model):
    """
    为选项框及选项文本内容创建的模型，目前没用处
    """
    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)

    select_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                       verbose_name=u"选项框的查找风格",
                                       help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                 u"link_text、partial_link_text、css_selector、xpath")
    select_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"选项框查找风格的确切值")
    select_option_text = models.CharField(max_length=300,default="",null=True, blank=True,
                                          verbose_name=u"选项的文本的内容")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"选项框及选项文本内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.select_ele_find_value


class AssertTipText(models.Model):
    """
    新增数据场景依赖的验证元素模型
    """
    newaddandcheck = models.ForeignKey(NewAddAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的添加场景",on_delete=models.PROTECT)

    tip_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"验证元素查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    tip_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"验证元素查找风格的确切值")
    tip_text = models.CharField(max_length=300,default="",null=True, blank=True,
                                  verbose_name=u"验证元素文本信息内容")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"验证元素相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.tip_ele_find_value


class SearchAndCheck(models.Model):#继承django的Model模块
    """
    查询场景
    """
    test_project = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    test_module = models.CharField(max_length=100, default="",null=True, blank=True, verbose_name=u"测试模块")
    test_page = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    case_priority = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("P0", u"冒烟用例"), ("P1", u"系统的重要功能用例") , ("P2", u"系统的一般功能用例"), ("P3", "极低级别的用例")),
                                     default="P1",
                                     verbose_name=u"用例优先级")
    test_case_title = models.CharField(max_length=200, default="", verbose_name=u"测试内容的名称")
    is_run_case = models.BooleanField(default=True,verbose_name=u"是否运行")
    depend_click_case = models.ForeignKey(ClickAndBack, default="", null=True, blank=True,
                                   verbose_name=u"依赖的点击场景的用例",on_delete=models.PROTECT)



    search_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                        verbose_name=u"查询按钮查找风格",
                                        help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                  u"link_text、partial_link_text、css_selector、xpath")
    search_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"查询按钮查找风格的确切值")
    is_with_date = models.BooleanField(default=True, verbose_name=u"是否查询到数据")
    result_table_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                             verbose_name=u"结果表格查找风格",
                                             help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                       u"link_text、partial_link_text、css_selector、xpath")
    result_table_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"结果表格查找风格的确切值")

    case_counts = models.IntegerField(default="1",verbose_name="循环次数",help_text=u"循环次数，请填写数字，"
                                                                   u"例如：1、2、3")
    write_user = models.ForeignKey(User,null=True, blank=True,verbose_name=u"添加人", on_delete=models.PROTECT)

    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"查询场景"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.test_case_title

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testdatas/searchandcheckcopy/{}/'>复制新加不带关联</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加不带关联"   #为go_to函数名个名字

    def go_to_with_relevance(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}/testdatas/searchandcheckcopywithrelevance/{}/'>复制新加</a>".format(DJANGO_SERVER_YUMING,self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to_with_relevance.short_description = u"复制新加"   #为go_to函数名个名字


class SearchInputTapInputText(models.Model):
    """
    查询场景依赖的文本输入框模型
    """
    searchandcheck = models.ForeignKey(SearchAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的搜素场景",on_delete=models.PROTECT)

    input_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                      verbose_name=u"输入框查找风格",
                                      help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                u"link_text、partial_link_text、css_selector、xpath")
    input_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"输入框查找风格的确切值")
    input_text = models.CharField(max_length=300,default="",null=True, blank=True,
                                  verbose_name=u"输入框中要输入的内容")
    search_result_colnum = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"在搜索结果表格中对应的列数",
                                            help_text=u"在搜索结果表格中对应的列数，请填写数字，例如：1、2、3;"
                                                      u"如果是多列，列数之间以半角逗号隔开，例如：3,4")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"文本输入框相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.input_ele_find_value


class SearchSelectTapSelectOption(models.Model):
    """
    查询场景依赖的选项框模型
    """
    searchandcheck = models.ForeignKey(SearchAndCheck,default="", null=True, blank=True,
                                   verbose_name=u"依赖的搜素场景",on_delete=models.PROTECT)
    select_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                       verbose_name=u"选项框的查找风格",
                                       help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                 u"link_text、partial_link_text、css_selector、xpath")
    select_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"选项框查找风格的确切值")
    select_option_ele_find = models.CharField(max_length=100, default="xpath",null=True, blank=True,
                                              verbose_name=u"选项的查找风格",
                                              help_text=u"元素查找风格：id、name、class_name、tag_name、"
                                                        u"link_text、partial_link_text、css_selector、xpath")
    select_option_ele_find_value = models.CharField(max_length=1000, default="",null=True, blank=True,
                                                         verbose_name=u"选项查找风格的确切值")
    search_result_colnum = models.CharField(max_length=100, default="", null=True, blank=True,
                                           verbose_name=u"在搜索结果表格中对应的列数",
                                            help_text=u"在搜索结果表格中对应的列数，请填写数字，例如：1、2、3...")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    add_time = models.DateTimeField(null=True, blank=True, auto_now_add=True,verbose_name=u"添加时间")
    # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,verbose_name=u"更新时间")

    class Meta:
        verbose_name = u"选项框相关内容"
        verbose_name_plural = verbose_name

    def __str__(self):#重载函数
        return self.select_ele_find_value





