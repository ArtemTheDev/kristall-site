from django.shortcuts import render, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.text import slugify


def russlug(slug):
    eng_letters = ['a', 'b', 'v', 'g', 'd', 'e', 'e', 'z', 'z', 'i', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't',
                   'u', 'f', 'h', 'ts', 'ch', 'sh', 'sh', 'ii', 'iii', 'iiii', 'ey', 'yu', 'ya']
    rus_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                   'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

    slugletters = []
    for i in range(len(slug)):
        slugletters += slug[i]
    for i in range(0, len(slugletters)):
        if slugletters[i] in rus_letters:
            slugletters[i] = eng_letters[rus_letters.index(slugletters[i])]
    slug = ''
    for i in slugletters:
        slug += i
    return slug


def home_page(request):
    return render(request, 'polls/home_page.html')


def news(request):
    tasks = Task.published.all()
    return render(request, 'polls/news.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def NewsPostDetail(request, post, id):
    post = get_object_or_404(Task, slug=post, status='published', id=request.user.id)
    return render(request, 'newsPostDetail.html', {'post': post})


def about(request):
    return render(request, 'polls/about.html')


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Task
    form_class = TaskForm
    template_name = 'polls/create_news.html'
    success_url = reverse_lazy('news')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = russlug(slugify(post.title, allow_unicode=True))
            print(russlug(slugify(post.title, allow_unicode=True)))
            post.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Гавно какоета")


@login_required
def profile(request):
    return render(request, 'account/profile.html')
