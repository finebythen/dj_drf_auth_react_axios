from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'age')
    def save_model(self, request, obj, form, change):
        if obj.id == None:
            obj.created_from = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)