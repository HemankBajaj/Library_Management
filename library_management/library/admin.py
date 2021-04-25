from django.contrib import admin
from .models import Book,Review, IssueRequest
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)

class ReviewAdmin(admin.ModelAdmin):
    pass
admin.site.register(Review, ReviewAdmin)

class IssueRequestAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssueRequest, IssueRequestAdmin)