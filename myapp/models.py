from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='news/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    view_news = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        ordering = ['created_at']

