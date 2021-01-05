from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Task
from .models import Customs


class Custom(admin.StackedInline):
    model = Customs


class UserAdmin(BaseUserAdmin):
    inlines = (Custom, )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author',)
    search_fields = ('title', 'task',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)