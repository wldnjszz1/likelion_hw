from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serialziers import PostSerialzers
from .permission import IsAuthorOrReadOnly, IsAuthorOrCantRead
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerialzers

    permission_classes = [
        # IsAuthorOrReadOnly,
        IsAuthorOrCantRead,
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # 로그인 한 유저의 리소스만 필터해서 보기
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs