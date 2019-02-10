from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Tag, Ingredient
from recipe import serializers


class BaseRecipeAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    """Base viewset for user owned attr."""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""

        return self.queryset.filter(user=self.request.user).order_by('-name')


class TagViewSet(BaseRecipeAttrViewSet):

    """Manage tags in the database """

    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializers


class IngredientViewSet(BaseRecipeAttrViewSet):

    """Manage ingredients in the database"""

    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
