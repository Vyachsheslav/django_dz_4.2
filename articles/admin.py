from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Tag, ArticleTag




class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_entry = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_entry += 1
            
            if main_entry != 1:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            
            
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
                raise ValidationError('Главный тег может быть только один')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = ArticleTag
    formset = RelationshipInlineFormset
    
    

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    
    inlines = [RelationshipInline]


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name']





