from django.db import models
from django.core.exceptions import ValidationError


class Tag(models.Model):
    
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, through='ArticleTag', related_name='article')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title





class ArticleTag(models.Model):
   
   article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_tags')
   tag = models.ForeignKey(Tag, on_delete=models.CASCADE,related_name='article_tags')
   is_main = models.BooleanField()
   


