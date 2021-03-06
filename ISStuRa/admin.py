from django.contrib import admin

from .models import Location, Typ, Time_between_replacement, Category, Inventary
# Register your models here.

class InventaryAdmin(admin.ModelAdmin):
    list_display = ('inventary_nr', 'objectname')
    search_fileds = ('inventary_nr', 'objectname')

admin.site.register(Location)
admin.site.register(Typ)
admin.site.register(Time_between_replacement)
admin.site.register(Category)
admin.site.register(Inventary, InventaryAdmin)
