from django.contrib import admin
from .models import Program, Package, Votes

admin.site.register(Program)
admin.site.register(Package)
admin.site.register(Votes)
