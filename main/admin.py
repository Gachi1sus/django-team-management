from django.contrib import admin
from .models import FactionMember, Faction

admin.site.register(Faction)
admin.site.register(FactionMember)
