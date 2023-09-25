from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(id=pk) # id 대신 pk, 서로 다른 pk
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    # article = Article()
    # article.title = request.GET.get('title')
    # article.content = request.GET.get('content')
    # article.save()


    article = Article(title=title, content=content)
    article.save()


    # Article.object.create(title=title, content=content)

    return render(request, 'articles/create.html')