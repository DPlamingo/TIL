from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm() # 클래스로 인스턴스를 만듬
#     context = {
#         'form': form,

#     }
#     return render(request, 'articles/new.html', context)


def create(request):
    if request.method == 'POST' :
    # 요청의 메서가 POST라면, creat 로직

        form = ArticleForm(request.POST)
        # 유효성 검사 진행
        if form.is_valid:
            # 유효성 검사가 통과된 경우,
            form.save()
            return redirect('articles:detail', Article.pk)
       
    # 아니라면, new 로직
    else:
        form = ArticleForm() # 클래스로 인스턴스를 만듬
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()
    # return redirect('articles:index')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect(request, 'articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    # update 부문
    if request.method == 'POST':  
        form = ArticleForm(request.POST, instance=article) # 인스턴스가 있네? 수정이구나~
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    # edit 부문
    else:
        form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    return redirect('articles:detail', context)
