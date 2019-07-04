from django.contrib import admin
from .models import CardNumber, CardExpiry, CardCode


@admin.register(CardNumber)
class CardNumberAdmin(admin.ModelAdmin):
    pass


@admin.register(CardExpiry)
class CardExpiryAdmin(admin.ModelAdmin):
    pass


@admin.register(CardCode)
class CardCodeAdmin(admin.ModelAdmin):
    pass
