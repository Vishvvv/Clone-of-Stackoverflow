from django.contrib import admin
from .models import Questions
# Register your models here.
@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')