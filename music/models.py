from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Music(models.Model):
    COUNTRY = (
        ('KG', 'Кыргызстан'),
        ('KZ', 'Казахстан'),
        ('RU', 'Россия')
    )
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='musics')
    country = models.CharField(max_length=50, choices=COUNTRY)
    duration = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title} ---- {self.category}'


    
    class Meta:
        db_table = 'product'
        verbose_name = 'Музыка'
        verbose_name_plural = 'Альбом'
