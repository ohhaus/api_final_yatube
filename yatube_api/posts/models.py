from django.contrib.auth import get_user_model
from django.db import models

from .constants import (
    COMMENT_CREATED_VERBOSE,
    COMMENT_STR_LENGTH,
    COMMENTS_RELATED_NAME,
    FOLLOWS_RELATED_NAME,
    GROUP_TITLE_MAX_LENGTH,
    POST_IMAGE_UPLOAD_PATH,
    POST_PUB_DATE_VERBOSE,
    POSTS_RELATED_NAME,
    UNIQUE_FOLLOW_CONSTRAINT,
)


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=GROUP_TITLE_MAX_LENGTH)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        POST_PUB_DATE_VERBOSE, auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to=POST_IMAGE_UPLOAD_PATH,
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        default_related_name = POSTS_RELATED_NAME

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )
    text = models.TextField()
    created = models.DateTimeField(
        COMMENT_CREATED_VERBOSE, auto_now_add=True, db_index=True
    )

    class Meta:
        default_related_name = COMMENTS_RELATED_NAME

    def __str__(self):
        return (
            'Комментарий {author} к посту {post_id}: {text}...'.format(
                author=self.author.username,
                post_id=self.post.pk,
                text=self.text[:COMMENT_STR_LENGTH]
            )
        )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name=UNIQUE_FOLLOW_CONSTRAINT
            )
        ]
        default_related_name = FOLLOWS_RELATED_NAME

    def __str__(self):
        return f'{self.user.username} подписан на {self.following.username}'
