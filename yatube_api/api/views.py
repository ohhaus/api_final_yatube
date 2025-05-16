from typing import Type

from django.db.models import QuerySet

from rest_framework import filters, mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsOwnerOrReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from posts.models import Follow, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с постами."""

    queryset: QuerySet[Post] = Post.objects.all()
    serializer_class: Type[PostSerializer] = PostSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer: PostSerializer) -> None:
        """Создает новый пост с текущим пользователем как автором."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для просмотра групп."""

    queryset: QuerySet[Group] = Group.objects.all()
    serializer_class: Type[GroupSerializer] = GroupSerializer
    permission_classes = (IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с комментариями."""

    serializer_class: Type[CommentSerializer] = CommentSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_post(self) -> Post:
        """Получает пост по post_id из параметров URL."""
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self) -> QuerySet:
        """Возвращает queryset комментариев для конкретного поста."""
        return self.get_post().comments.all()

    def perform_create(self, serializer: CommentSerializer) -> None:
        """Создает новый комментарий с привязкой к посту и автору."""
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """Вьюсет для работы с подписками."""

    serializer_class: Type[FollowSerializer] = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self) -> QuerySet[Follow]:
        """Возвращает queryset подписок текущего пользователя."""
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer: FollowSerializer) -> None:
        """Создает подписку от имени текущего пользователя."""
        serializer.save(user=self.request.user)
