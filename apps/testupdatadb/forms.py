from django import forms    #导入django中的forms

# from .models import ClickAndBack,NewAddAndCheck,SearchAndCheck,DeleteAndCheck,EditAndCheck  #导入ClickAndBack模块
# from .models import LoginAndCheck


# class LoginAndCheckForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
#     class Meta:
#         model = LoginAndCheck   #指明转换的QSLoginAndCheck
#         fields = "__all__"
#
#
# class ClickAndBackForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
#     class Meta:
#         model = ClickAndBack   #指明转换的QSClickAndBack
#         fields = "__all__"
#         # fields = ['test_project','test_module','test_page','requirement_function','case_priority',
#         #          'case_process_type', 'case_title','case_precondition', 'case_step', 'case_expected_result',
#         #           'write_comments','write_user','write_case_time']  #指明要转换的字段
#
#
# class NewAddAndCheckForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
#     class Meta:
#         model = NewAddAndCheck   #指明转换的QSClickAndBack
#         fields = "__all__"
#
#
#
# class SearchAndCheckForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
#     class Meta:
#         model = SearchAndCheck  #指明转换的QSSearchAndCheck
#         fields = "__all__"
#
#
# class DeleteAndCheckForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
#     class Meta:
#         model = DeleteAndCheck   #指明转换的QSDeleteAndCheck
#         fields = "__all__"
#
#
#
# class EditAndCheckForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
#     class Meta:
#         model = EditAndCheck   #指明转换的QSEditAndCheck
#         fields = "__all__"
