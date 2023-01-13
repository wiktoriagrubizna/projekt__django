from django.contrib import admin

from .models import Actor
admin.site.register(Actor)

from .models import Director
admin.site.register(Director)

from .models import Ocena
admin.site.register(Ocena)

from .models import Film
admin.site.register(Film)

