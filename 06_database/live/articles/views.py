from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    # request.method == 'POST' 를 조건으로 잡고 나머지 else처리였는데,
    # POST 이외 요청에 대해서는 DB에 영향을 미치지 않는 HTML 반환처리
    # 얘는 왜 GET 이랑 POST를 if elif로 처리하나요?
    # GET일 때, POST일 때 정해진 상황에 대해 정해진 처리만 하면 그만
    if request.method == 'GET':
        # [<Article Object (1)>, <Article Object(2)>,...]
        articles = Article.objects.all()
        # articles에 들어있는 데이터들을 HTML에 그려서 반환
        # articles에 들어있는 데이터들을 JSON으로 변환해서 반환
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
