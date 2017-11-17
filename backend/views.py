from django.shortcuts import render,redirect
from myblog.models import article
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from backend.form import LoginForm, PostForm
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


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


class Manager(TemplateView):
    template_name = 'backend-index.html'

    @method_decorator(login_required(login_url='/manager/login/'))
    def dispatch(self, *args, **kwargs):
        return super(Manager, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Manager, self).get_context_data(**kwargs)
        context['postlist'] = article.objects.all().order_by("-id")
        return context


class ChangePost(FormView):
    def get(self, request, id):
        form = PostForm()
        return render(request, 'change-post.html', {'form': form})

    @method_decorator(login_required(login_url='/manager/login/'))
    def dispatch(self, *args, **kwargs):
        return super(ChangePost, self).dispatch(*args, **kwargs)

