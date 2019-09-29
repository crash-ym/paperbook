from django.contrib import admin
from aper.models import PaperUser,Author,BookInfo,TagBook
# Register your models here.
class PaperUserAdmin(admin.ModelAdmin):
    list_display = ['name','passwd','email']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['authorName','contry','describ','masterpiece','link']

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['bookName','authorName','bookTag','bookLink','bookDes']

class TagBookAdmin(admin.ModelAdmin):
    list_display = ['tagBid','tagName']

admin.site.register(PaperUser,PaperUserAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(TagBook,TagBookAdmin)
