from django.contrib import admin
from apps.home.models import (
    Home, Service, Partners,
    Price, Team, FAQ,
    About, AboutService,Benefits,
    Contact
)


admin.site.register(Home)
admin.site.register(Service)
admin.site.register(Price)
admin.site.register(Partners)
admin.site.register(Team)
admin.site.register(FAQ)
admin.site.register(About)
admin.site.register(AboutService)
admin.site.register(Benefits) 
admin.site.register(Contact)
 