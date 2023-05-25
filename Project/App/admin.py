from django.contrib import admin
from .models import Post
# Register your models here.

#Cela permettra d'appliquer les personnalisations spécifiées dans la classe PostAdmin lors de l'administration du modèle Post dans la partie d'administration de Django.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    
#model.ModelAdmin contient des fonctionnalitees integrees par django pour gerer l'interface de notre Post dans admin  

admin.site.register(Post, PostAdmin)