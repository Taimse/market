from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Items, ItemAdmin)
admin.site.register(Categories)
admin.site.register(Basket)