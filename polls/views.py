from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from django.template import loader
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from polls.serializers import UserSerializer, GroupSerializer
from fileoperation.models import UploadFileForm
# Create your views here.


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['file'])
            #handle_upload_file(form.files['file'])
            return HttpResponse('upload success!')
    else:
        form = UploadFileForm()
    return render(request, 'polls/../templates/upload.html', {'form': form})


def handle_upload_file(file):
    with open("/tmp/%s" % file.name, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)

class TestView(APIView):  # CBV模式的视图函数

    def get(self, request, *args, **kwargs):
        # 定义get方法
        # 在django-rest-framework中的request被重新封装了，后续分析源码的时候会有具体体现
        return Response('测试api')  # rest-framework的模板对数据进行渲染



def loadView(request):
    template_name = 'polls/upload.html'
    #
    # render(request=None, template_name=template_name, context={})
    return render(request=None, template_name=template_name, context={})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



from django.shortcuts import render,HttpResponse
from .models import Imgs_name,Imgs
import random

def up_imgs(request):
    return render(request, 'polls/up_imgs.html')

def upload_imgs(request):
    '''
        model拆分成2个表，其中一个为文件存储，一个为图集
        图集对文件存储中需要有一个字段设置为多对多的储存关系
        post后获得文件
        先对图集实例化，增加其他字段应填写的值，对这个实例存储
        再对多文件列表循环，对图片本身实例化，增加其他字段应填写的值，再对这个实例存储
        最后添加图片对应图集的关系表保存
    :param request:
    :return:
    '''
    test = Imgs_name()
    test.name = 'test' + str(random.randint(100, 900))
    test.save()
    for f in request.FILES.getlist('imgs'):
        print(f)
        empt = Imgs()
        # 增加其他字段应分别对应填写
        empt.single=f
        empt.img=f
        empt.save()
        test.imgs.add(empt)

        # File(file=f, files=test,id=1).save()
    return HttpResponse('上传成功')