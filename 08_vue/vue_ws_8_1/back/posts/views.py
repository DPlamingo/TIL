from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response # 반환방법은 rest framework에서 정의한대로 반환
from rest_framework.decorators import api_view
from .models import Post, Category
from .serializers import PostListSerializer, PostSerializer, CategorySerializer

# Create your views here.
@api_view(['GET'])
def category_list(request):
    categories = Category.object.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    


# GET을 posts에 해줄 데코레이터가 필요하다.
@api_view(['GET', 'POST'])
def post_list_created(request):
    if request.method == 'GET':
        # 모든 post정보를 요청자에게 넘겨준다.
        posts = Post.objects.all()
        # posts 리스트에 들어있는 각 post 정보들중
        # 사용자에게 넘겨줄 pk, title, content
        serializers = PostListSerializer(posts, many=True)
        # 정보만 정리한 dictionary 자료를 JSON으로 변환해서 반환해야함.
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        category = Category.objects.get(pk=request.data.get('category'))
        if serializer.is_valid(raise_exception=True):
            serializer.save(category=category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# def post_detail(request, post_pk):
#     # 일반적인 pk기준 조회
#     # post = Post.objects.get(pk=post_pk)
#     # 조회 대상 검색시, 대상이 있으면 객체 반환 없으면 404 status 반환
#     post = get_object_or_404(Post,pk=post_pk)
#     # db에서 pk기준으로 찾아온 객체 정보가 가진 모든 필드를 serializer한다.
#     serializer = PostSerializer(post)
#     return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail_update_delete(request, post_pk):
    # 일반적인 pk기준 조회
    # post = Post.objects.get(pk=post_pk)
    # 조회 대상 검색시, 대상이 있으면 객체 반환 없으면 404 status 반환
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        # db에서 pk기준으로 찾아온 객체 정보가 가진 모든 필드를 serialzer화 한다.
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(data=request.data, instance=post)
        category = Category.objects.get(pk=request.data.get('category'))
        # 유효성 검사(유효성 통과 못할 시, 400 예외상황 발생시키기)
        if serializer.is_valid(raise_exception=True):
            serializer.save(category=category)
            return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        data = {
            'pk': post_pk,
            'message': f'{post_pk}번 게시글은 삭제 되었습니다.'
        }
        return Response(data=data)