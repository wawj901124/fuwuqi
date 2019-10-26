import xadmin

from .models import  Report,RequestReport


class ReportAdmin(object):
    ziduan = ['reportname', 'reportfile']

    list_display =['testproject','testmodule','reportname', 'go_to','add_time','update_time']#定义显示的字段
    search_fields =  ['testproject','testmodule','reportname','reportfile',]   #定义搜索字段
    list_filter =  ['testproject','testmodule','reportname','reportfile',] #定义筛选的字段
    model_icon = 'fa fa-bars '  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ['id','testproject','testmodule','reportname', 'reportfile','add_time','update_time',]  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    # list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = []   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    # show_detail_fields = []   #显示数据详情



class RequestReportAdmin(object):
    ziduan = ['id','testproject','testmodule',
              'testpage',
                   'testcasetitle','teststarttime',
                   'forcount',
              'test_result',
              'response_status_code',
                   'response_text','response_content',
              'response_json',
                   'response_elapsed','response_elapsed_microseconds',
                   'response_headers','response_cookies',
                   'add_time','update_time']

    list_display =['testproject','testmodule',
                   'testpage',
                   'testcasetitle','teststarttime',
                   'forcount',
                   'test_result',
                   'response_status_code',
                   'response_text',
                   'response_json',
                   'response_elapsed','response_elapsed_microseconds',
                   'response_headers','response_cookies',
                   'add_time','update_time']#定义显示的字段
    search_fields =  ['testproject','testmodule',
                   'testcasetitle','teststarttime',
                      'response_text','response_content',
                      'response_headers','response_cookies']   #定义搜索字段
    list_filter =  ['testproject','testmodule',
                   'testcasetitle','teststarttime',] #定义筛选的字段
    model_icon = 'fa fa-bars '  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ziduan  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    # list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = []   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    # show_detail_fields = []   #显示数据详情
    data_charts = {   #使用网址：https://xadmin.readthedocs.io/en/latest/_modules/xadmin/plugins/chart.html
                      # 插件介绍网址：http://www.mamicode.com/info-detail-2403646.html
                      #使用网址：https://www.jianshu.com/p/6201e1e9133c
        "user_count": {'title': u"接口响应时间", "x-field": "forcount", "y-field": ('response_elapsed_microseconds',),
                       "order": ('id',)},
    }



xadmin.site.register(Report, ReportAdmin) #在xadmin中注册Report
xadmin.site.register(RequestReport, RequestReportAdmin) #在xadmin中注册Report