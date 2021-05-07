from django.contrib import admin
from .models import Post

@admin.register(Post) # registrando modelo
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)} # enquanto escreve o título, escreve o slug automaticamente