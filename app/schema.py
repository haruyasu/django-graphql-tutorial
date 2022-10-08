import graphene
from graphene_django import DjangoObjectType
from .models import Post


class PostType(DjangoObjectType):
  class Meta:
    model = Post


class Query(graphene.ObjectType):
  all_posts = graphene.List(PostType)

  def resolve_all_posts(root, info, **kwargs):
    return Post.objects.order_by("-id")
