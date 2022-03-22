from django.db import models


class Track(models.Model):
    track = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.track

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'


class Text(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    text = models.TextField('Текст трека')
    pub_date = models.DateTimeField('Дата выхода')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'


class Comment(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=200)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.author_name
