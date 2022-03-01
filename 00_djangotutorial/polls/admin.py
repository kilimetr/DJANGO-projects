from django.contrib import admin
from polls.models import Question, Choice



class ChoseInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, 
            {"fields": ["question_text"]}),
        ("Date information", 
            {"fields": ["pub_date"]}),
    ]

    inlines = [ChoseInline]

    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]

    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

