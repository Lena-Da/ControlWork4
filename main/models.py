from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps = models.TextField()
    cook_time = models.IntegerField(default=0)
    image = models.ImageField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
