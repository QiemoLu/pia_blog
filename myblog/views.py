#coding:utf-8
from django.shortcuts import render
from myblog.models import article
from django.http import Http404
from myblog.models import aboutme
from django.views.generic.dates import MonthArchiveView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.shortcuts import redirect
from django.db.models import Q
# Create your views here.


def index(request):
    # all()是一个列表，需要遍历
    postlist = article.objects.all().order_by("-id")  # 按照文章时间降序
    paginator = Paginator(postlist, 4)  # 每页显示2 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        postlist = paginator.page(page)
    except PageNotAnInteger:  # 如果页码不是个整数
        postlist = paginator.page(1)  # 取第一页记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        postlist = paginator.paginator(paginator.num_pages)  # 取最后一页的记录
    return render(request, 'index.html', {"postlist": postlist})


def detail(request, id):  # 接受url传入的id
    try:
        post = article.objects.get(id=str(id))  # 以id为主键获取文章
    except article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {"post": post})


def about(request):
    about = aboutme.objects.all()
    return render(request, 'aboutme.html', {"about": about})


def Category_list(request, category):
    try:
        category_post = article.objects.filter(category__name__iexact=category).order_by('-id')
        if not category_post.exists():
            return render(request, 'category.html', {'error': True})
        paginator = Paginator(category_post, 4)
        page = request.GET.get('page')
        try:
            category_post = paginator.page(page)
        except PageNotAnInteger:
            category_post = paginator.page(1)
        except EmptyPage:
            category_post = paginator.paginator(paginator.num_pages)
    except article.DoesNotExist:
        raise Http404
    return render(request, 'category.html', {
        "category_post": category_post,
        "error": False})


def search(request):
    q = request.GET.get('q', '')
    if q:
        # icontains是一个查询关键字 此字段仅在标题中查找
        w = Q(title__icontains=q)
        search_post = article.objects.filter(w).distinct()
        if len(search_post) == 0:
            return render(request, 'search.html', {'error': True})
        else:
            return render(request, 'search.html', {
                "search_post": search_post,
                'error': False})
    return redirect('/')


class MonthArchiveView(MonthArchiveView):
    model = article
    template_name = 'archives.html'
    # contest_object_name用于指定上下文变量
    context_object_name = "article_list"
    date_field = "createtime"
    # 允许显示超过当前日期的对象，即未来日期的对象
    # 假如现在时间是2016年，可以允许指定日期为2017的对象显示
    allow_future = True
    year_format = '%Y'
    month_format = '%m'
