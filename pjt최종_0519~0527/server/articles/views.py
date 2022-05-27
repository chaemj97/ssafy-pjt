from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Article,Comment
from rest_framework.decorators import api_view
from .serializers import ArticleListSerializer,CommentSerializer,ArticleSerializer
from rest_framework.response import Response
from rest_framework import status

@ api_view(['GET','POST'])
def article_list(request):
    # article 목록 반환
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles,many=True)
        return Response(serializer.data)
    
    # article 생성
    elif request.method == 'POST':
        user=request.user
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
def article_detail(request,article_pk):
    # article 조회, 생성, 삭제
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article,data=request.data)
        user=request.user
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete':f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def article_like(request,article_pk):
    # 로그인 했을때만
    # 1. 좋아요 누른 게시글, 사용자 정보 가져오기
    article = get_object_or_404(Article,pk=article_pk)
    user = request.user
    # 2.좋아요 취소
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
    # 3. 좋아요 추가
    else:
        article.like_users.add(user)
    serializer = ArticleSerializer(article)
    return Response(serializer.data,status=status.HTTP_200_OK)


# 댓글

@ api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments,many=True)
    return Response(serializer.data)

@ api_view(['GET','PUT','DELETE'])
def comment_detail(request,article_pk,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    article = get_object_or_404(Article,pk=article_pk)
    user = request.user
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article,user=user)
            return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete':f'데이터 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)

@ api_view(['POST'])
def comment_create(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    user=request.user
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article,user=user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)



