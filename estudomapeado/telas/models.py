from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class CategoryTexto(models.Model):
    name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('categoria_textos', args=[self.id])

    # Fazendo a mudança do nome na pagina do admin
    class Meta:
        verbose_name_plural = "CategoriasTexto"

    def __str__(self):
        return self.name


class CategoryVideo(models.Model):
    name = models.CharField(max_length=30)

    # Fazendo a mudança do nome na pagina do admin
    class Meta:
        verbose_name_plural = "CategoriasVideo"

    def __str__(self):
        return self.name


class Texto(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    link = models.URLField(max_length=200, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField("CategoryTexto", related_name="textos")

    # novamente mudança do nome para ficar mais facil a referenciação
    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    link = models.URLField(max_length=200, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("CategoryVideo", related_name="videos")


class ForumMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
