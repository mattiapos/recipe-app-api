from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Ingredient, Tag
from recipe import serializers


class BaseRecipeAttrViewSet(viewsets.GenericViewSet,
                            mixins.CreateModelMixin,
                            mixins.ListModelMixin):
    """
    Base viewset for user owned recipe attributes.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Return objects for the current authenticated user only.
        """
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """
        Create a new tag.
        """
        serializer.save(user=self.request.user)


class TagViewset(BaseRecipeAttrViewSet):
    """
    Manage Tags in the database.
    """
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewset(BaseRecipeAttrViewSet):
    """
    Manage Ingredients in the database.
    """
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
