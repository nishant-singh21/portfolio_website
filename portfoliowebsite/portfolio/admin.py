from django.contrib import admin

from .models import ContactMessage, SiteProfile


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

    def has_add_permission(self, request):
        return False


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated_at')
    readonly_fields = ('updated_at',)

    def has_add_permission(self, request):
        return not SiteProfile.objects.exists()


admin.site.site_header = 'Nishant Singh — Portfolio Admin'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Site administration'
