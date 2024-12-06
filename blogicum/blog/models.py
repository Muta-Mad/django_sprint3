

from django.db import models

from django.contrib.auth import get_user_model


USER = get_user_model()


class Base(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name='Заголовок'
    )
    is_published = models.BooleanField(
        default=True,
        blank=False,
        null=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True


class Post(Base):
    text = models.TextField(
        blank=False,
        null=False,
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — '
                  'можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        USER, on_delete=models.CASCADE,
        null=False,
        verbose_name='Автор публикации',

    )
    location = models.ForeignKey(
        'Location', on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение',

    )
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL,
        blank=False,
        null=True,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'


class Category(Base):
    description = models.TextField(
        blank=False,
        null=False,
        verbose_name='Описание'
    )
    slug = models.SlugField(
        unique=True,
        blank=False,
        null=False,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы '
                  'латиницы, цифры, дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(Base):
    name = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        verbose_name='Название места'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'
