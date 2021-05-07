from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255) 
    #charfield-> campo com strings que aguenta até 255 cacteres
    slug = models.SlugField(max_length=255, unique=True)
    # www.meu.site.com/blog/introducao-ao-blog -> slugfield: introducao-ao-blog
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # referência ao id do usuário(outra classe) -> author
    # on_delete=models.CASCADE -> se o usuário for deletado, o post também é deletado
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True -> data e hora do post criado colocado automaticamente 
    updated = models.DateTimeField(auto_now=True)
    # auto_now_add=True -> data e hora do post editado colocado automaticamente

    class Meta:
        ordering = ('-created',) # organiza as postagens dos mais recentes pros mais antigos

    def __str__(self):
        return self.title

    def get_absolute_url(self): # definindo a url de um post
        return reverse('blog:detail', kwargs={'slug': self.slug})