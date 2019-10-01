from django.shortcuts import render
from django.views.generic import View   #导入View


from .models import ClickAndBack,User,NewAddAndCheck,SearchAndCheck   #ClickAndBack
from .forms import ClickAndBackForm,NewAddAndCheckForm,SearchAndCheckForm  #导入QSClickAndBackForm
from wanwenyc.settings import DJANGO_SERVER_YUMING



# Create your views here.
#添加场景的view
class  ClickAndBackView(View):  #继承View
    """
    测试数据复制编写页面处理
    """
    def get(self,request,clickandback_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html",{
                "django_server_yuming":DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            clickandback = ClickAndBack.objects.get(id=int(clickandback_id))   #获取用例
            clickandback_all = ClickAndBack.objects.all().order_by("-id")
            return render(request,"clickAndBack.html",
                          {"clickandback":clickandback,
                           "clickandback_all":clickandback_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           })
        else:
            return render(request,"addContentError.html",{
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,clickandback_id):
        username = request.user.username
        clickandback_all = ClickAndBack.objects.all().order_by("-id")
        clickandback_form = ClickAndBackForm(request.POST)  # 实例化ClickAndBackForm()
        clickandback = ClickAndBack.objects.get(id=int(clickandback_id))  # 获取用例

        if clickandback_form.is_valid():  # is_valid()判断是否有错

            clickandback_form.save(commit=True)  # 将信息保存到数据库中

            zj = ClickAndBack.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            clickandbackid = zj.id
            clickandbackadd = ClickAndBack.objects.get(id=int(clickandbackid))  # 获取用例
            return render(request, "clickAndBack.html", {
                "clickandback": clickandbackadd,
                "clickandback_all": clickandback_all,
                "sumsg":u"添加测试用例---【{}】---成功,请继续添加".format(clickandbackadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })
        else:
            return render(request, 'clickAndBackForm.html', {
                "clickandback": clickandback,
                "clickandback_all": clickandback_all,
                "clickandbackform": clickandback_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })  # 返回页面，回填信息

#新增场景的view
class  NewAddAndCheckView(View):  #继承View
    """
    测试数据复制编写页面处理
    """
    def get(self,request,newaddandcheck_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html",{
                "django_server_yuming":DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            newaddandcheck = NewAddAndCheck.objects.get(id=int(newaddandcheck_id))   #获取用例
            clickandback_all = ClickAndBack.objects.all().order_by("-id")
            return render(request,"newaddandcheck/newAddAndCheck.html",
                          {"newaddandcheck":newaddandcheck,
                           "clickandback_all":clickandback_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           })
        else:
            return render(request,"addContentError.html",{
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,newaddandcheck_id):
        username = request.user.username
        clickandback_all = ClickAndBack.objects.all().order_by("-id")
        newaddandcheck_form = NewAddAndCheckForm(request.POST)  # 实例化NewAddAndCheckForm()
        newaddandcheck = NewAddAndCheck.objects.get(id=int(newaddandcheck_id))  # 获取用例

        if newaddandcheck_form.is_valid():  # is_valid()判断是否有错

            newaddandcheck_form.save(commit=True)  # 将信息保存到数据库中

            zj = NewAddAndCheck.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            newaddandcheckid = zj.id
            newaddandcheckadd = NewAddAndCheck.objects.get(id=int(newaddandcheckid))  # 获取用例
            return render(request, "newaddandcheck/newAddAndCheck.html", {
                "newaddandcheck": newaddandcheckadd,
                "clickandback_all": clickandback_all,
                "sumsg":u"添加测试用例---【{}】---成功,请继续添加".format(newaddandcheckadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })
        else:
            return render(request, 'newaddandcheck/newAddAndCheckForm.html', {
                "newaddandcheck": newaddandcheck,
                "clickandback_all": clickandback_all,
                "newaddandcheckform": newaddandcheck_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })  # 返回页面，回填信息


#查询场景的view
class  SearchAndCheckView(View):  #继承View
    """
    测试数据复制编写页面处理
    """
    def get(self,request,searchandcheck_id):
        if request.user.username == 'check':
            return render(request, "canNotAddclickAndBack.html",{
                "django_server_yuming":DJANGO_SERVER_YUMING
            })
        elif request.user.is_active:
            searchandcheck = SearchAndCheck.objects.get(id=int(searchandcheck_id))   #获取用例
            clickandback_all = ClickAndBack.objects.all().order_by("-id")
            return render(request,"searchandcheck/searchAndCheck.html",
                          {"searchandcheck":searchandcheck,
                           "clickandback_all":clickandback_all,
                           "django_server_yuming": DJANGO_SERVER_YUMING,
                           })
        else:
            return render(request,"addContentError.html",{
                "django_server_yuming": DJANGO_SERVER_YUMING
            })

    def post(self, request,searchandcheck_id):
        username = request.user.username
        clickandback_all = ClickAndBack.objects.all().order_by("-id")
        searchandcheck_form = SearchAndCheckForm(request.POST)  # 实例化SearchAndCheckForm()
        searchandcheck = SearchAndCheck.objects.get(id=int(searchandcheck_id))  # 获取用例

        if searchandcheck_form.is_valid():  # is_valid()判断是否有错

            searchandcheck_form.save(commit=True)  # 将信息保存到数据库中

            zj = SearchAndCheck.objects.all().order_by('-add_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            searchandcheckid = zj.id
            searchandcheckadd = SearchAndCheck.objects.get(id=int(searchandcheckid))  # 获取用例
            return render(request, "searchandcheck/searchAndCheck.html", {
                "searchandcheck": searchandcheckadd,
                "clickandback_all": clickandback_all,
                "sumsg":u"添加测试用例---【{}】---成功,请继续添加".format(searchandcheckadd.test_case_title),
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })
        else:
            return render(request, 'searchandcheck/searchAndCheckForm.html', {
                "searchandcheck": searchandcheck,
                "clickandback_all": clickandback_all,
                "searchandcheckform": searchandcheck_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
                "django_server_yuming": DJANGO_SERVER_YUMING,
            })  # 返回页面，回填信息