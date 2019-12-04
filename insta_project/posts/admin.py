from django.contrib import admin

from .models import Post

admin.site.register(Post)


from actions import export_as_csv
class MyAdmin(admin.ModelAdmin):
    actions = [export_as_csv]

