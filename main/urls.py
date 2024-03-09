from django import urls
from .views import *

urlpatterns = [
    urls.path('', index, name='home'),
    urls.path('recipe/add/', add, name='add'),
    urls.path('recipe/<int:recipe_id>/', recipe, name='recipe'),
    urls.path('recipe/<int:recipe_id>/change/', change, name='change'),
]
