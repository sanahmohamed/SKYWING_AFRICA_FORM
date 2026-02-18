from django.contrib import admin
from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = [
        'full_name', 'contact_number', 'email', 'nationality',
        'budget', 'property_type', 'date_of_attending', 'time_slot', 'submitted_at'
    ]
    list_filter = ['budget', 'property_type', 'date_of_attending', 'time_slot', 'submitted_at']
    search_fields = ['full_name', 'email', 'contact_number', 'nationality']
    readonly_fields = ['submitted_at', 'ip_address']
    ordering = ['-submitted_at']

    fieldsets = (
        ('Personal Information / 个人信息', {
            'fields': ('full_name', 'contact_number', 'email', 'nationality')
        }),
        ('Property Preferences / 房产偏好', {
            'fields': ('budget', 'property_type')
        }),
        ('Visit Schedule / 参观安排', {
            'fields': ('date_of_attending', 'time_slot')
        }),
        ('Additional / 其他', {
            'fields': ('reference',)
        }),
        ('Metadata', {
            'fields': ('submitted_at', 'ip_address'),
            'classes': ('collapse',)
        }),
    )

    def get_export_filename(self, file_format):
        return f'skywing_registrations.{file_format}'
