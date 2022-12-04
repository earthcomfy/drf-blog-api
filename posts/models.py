from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("Category name"), max_length=100)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(_("Post title"), max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        null=True,
        on_delete=models.SET_NULL,
    )
    categories = models.ManyToManyField(Category, related_name="posts_list", blank=True)
    body = models.TextField(_("Post body"))
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="post_likes", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.title} by {self.author.username}"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="post_comments",
        null=True,
        on_delete=models.SET_NULL,
    )
    body = models.TextField(_("Comment body"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.body[:20]} by {self.author.username}"
