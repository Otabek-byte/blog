from django.contrib import admin
from .models import Question, Choice


# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text', 'file']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']})

    ]
    inlines = [ChoiceInLine]





admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

