from django.contrib import admin

from data.models import Gym, Subscription, Address, Customer


class AddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'phone')
    list_filter = ('city', 'street',)
    search_fields = ('city', 'street', 'phone')
    ordering = ['city']


admin.site.register(Address, AddressAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'phone_number', 'subscription', )
    list_filter = ('surname', 'name', 'phone_number', 'subscription', )
    search_fields = ('surname', 'name', 'phone_number', 'subscription')
    ordering = ['surname']


admin.site.register(Customer, CustomerAdmin)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscription_number', 'name', 'is_active')
    list_filter = ('name', 'is_active')


admin.site.register(Subscription, SubscriptionAdmin)


class GymAdmin(admin.ModelAdmin):
    list_display = ('address', )
    list_filter = ('address', 'customers', 'opened_at')
    search_fields = ('address', )
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    ordering = ['address']

    # def get_phone(self, obj):
    #     return obj.address.phone


admin.site.register(Gym, GymAdmin)
