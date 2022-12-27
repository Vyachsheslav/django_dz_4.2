from django.contrib import admin

from .models import Article, Tag, Scope

class RelationshipInline(admin.TabularInline):
    model = Scope
    
    

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    
    inlines = [RelationshipInline]


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name']





