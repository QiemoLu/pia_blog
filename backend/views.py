from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView
from myblog.models import article, Category, aboutme
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from backend.form import LoginForm, PostForm, CategoryForm, AboutMeForm

# Create your views here.


class LoginRequired(View):
    @method_decorator(login_required(login_url='/manager/login/'))
    def dispatch(self, *args, **kwargs):
        return super(LoginRequired, self).dispatch(*args, **kwargs)



class LoginView(FormView):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("name", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user:
                login(request, user)
                return redirect('/manager/index')
            login_form.add_error('password', '用户名或密码错误')

        return render(request, 'login.html', {'form':login_form})

class LoginOut(TemplateView):
    def get(self, request):
        logout(request)
        return redirect('/manager/login')


class Manager(TemplateView, LoginRequired):
    template_name = 'backend-index.html'

    def get_context_data(self, **kwargs):
        context = super(Manager, self).get_context_data(**kwargs)
        context['postlist'] = article.objects.all().order_by("-id")
        return context


class ChangePost(FormView, LoginRequired):
    page_title = "修改文章"

    def get(self, request, id):
        article_obj = get_object_or_404(article, id=str(id))

        data = {'title':article_obj.title, 'category': article_obj.category,
                'context': article_obj.content}
        form = PostForm(initial=data)
        return render(request, 'change-post.html', {'form': form, 'page_title':
            self.page_title})

    def post(self, request, id):
        form = PostForm(request.POST)
        if form.is_valid():
            title = request.POST.get("title", "")
            category = request.POST.get("category", "")
            context = request.POST.get("context", "")
            article.objects.filter(id=str(id)).update(
                    title=title,
                    category=category,
                    content=context)
            return redirect('/manager/index')
        return render(request, 'change-post.html', {'form': form,
            'page_title':self.page_title})


class PostAdd(FormView, LoginRequired):
    page_title = "添加文章"

    def get(self, request):
        form = PostForm()
        return render(request, 'change-post.html',{'form': form,
            'page_title': self.page_title})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            title = request.POST.get("title", "")
            category = request.POST.get("category", "")
            context = request.POST.get("context", "")
            article.objects.create(
                    title=title,
                    category=Category.objects.get(id=str(category)),
                    content=context)

            return redirect('/manager/index')
        return render(request, 'change-post.html',{'form': form,
            'page_title': self.page_title})


class CategoryList(TemplateView, LoginRequired):
    template_name = 'backend-category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['postlist'] = Category.objects.all().order_by("-id")
        return context


class CategoryChange(FormView, LoginRequired):
    page_title = "修改标签"
    def get(self, request, id):
        category_obj = get_object_or_404(Category, id=str(id))
        data = {'name':category_obj.name}
        form = CategoryForm(initial=data)
        return render(request, 'change-category.html',{'form': form,
            'page_title': self.page_title})

    def post(self,request, id):
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name", "")
            Category.objects.filter(id=str(id)).update(name=name.strip())
            return redirect('/manager/category')
        return render(request, 'change-category.html',{'form': form,
            'page_title': self.page_title})


class CategoryAdd(FormView, LoginRequired):
    page_title = "添加标签"

    def get(self, request):
        form = CategoryForm()
        return render(request, 'change-category.html',{'form': form,
            'page_title': self.page_title})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name", "")
            Category.objects.create(
                    name=name.strip())

            return redirect('/manager/category')
        return render(request, 'change-category.html',{'form': form,
            'page_title': self.page_title})

@login_required(login_url='/manager/login/')
def delete_post(request, id):
    article_obj = get_object_or_404(article, id=str(id))
    article_obj.delete()
    return redirect('/manager/index')


@login_required(login_url='/manager/login/')
def delete_category(request, id):
    category_obj = get_object_or_404(Category, id=str(id))
    category_obj.delete()
    return redirect('/manager/category')

class AboutMe(TemplateView, LoginRequired):
    page_title = "添加"
    aboutme_obj = aboutme.objects.filter()

    def get(self, request):
        data= {}
        if self.aboutme_obj.exists():
            data = {'aboutme':self.aboutme_obj[0].aboutme}
        form = AboutMeForm(initial=data)
        return render(request, 'backend-aboutme.html',{'form': form,
            'page_title': self.page_title})

    def post(self, request):
        form = AboutMeForm(request.POST)
        if form.is_valid():
            aboutme = request.POST.get("aboutme", "")
            if self.aboutme_obj.exists():
                self.aboutme_obj.update(aboutme=aboutme)
            else:
                self.aboutme_obj.create(aboutme=aboutme)

            return redirect('/aboutme')
        return render(request, 'backend-aboutme.html',{'form': form,
            'page_title': self.page_title})

