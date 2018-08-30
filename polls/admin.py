from django.contrib import admin
from .models import Question, Choice


# Register your models here.
# class ChoiceInline (admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    # 有三个关联的选项插槽——由 extra 定义，且每次你返回任意已创建的对象的“修改”页面时，你会见到三个新的插槽。
    # 在三个插槽的末端，你会看到一个“添加新选项”的按钮。
    # 如果你单击它，一个新的插槽会被添加。如果你想移除已有的插槽，可以点击插槽右上角的X。注意，你不能移除原始的 3 个插槽
    # 不过，仍然有点小问题。它占据了大量的屏幕区域来显示所有关联的 Choice 对象的字段。
    # 对于这个问题，Django 提供了一种表格式的单行显示关联对象的方法。
    # 通过 TabularInline``（替代 ``StackedInline ），关联对象以一种表格式的方式展示，显得更加紧凑


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # 添加槽位
    inlines = [ChoiceInline]
    # 添加过滤器，根据pub_date进行过滤
    list_filter = ['pub_date']
    # 添加查询搜索框
    search_fields = ['question_text']
    # 添加分页
    list_per_page = 3
    # 日期层次结构
    date_hierarchy = 'pub_date'


    list_display = ('question_text', 'pub_date', 'was_published_recently')


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
