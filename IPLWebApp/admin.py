from django.contrib import admin
from .models import addTeam, Banglore, delhi, mumbai, hyderabad, chennai, kolkata, punjab, rajasthan, addNewPlayers


# Register your models here.


class Bangaloreadmin(admin.ModelAdmin):
    list_display = ['player_name', 'role', 'price', 'status', 'team']
admin.site.register(Banglore, Bangaloreadmin)


class ChennaiAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'role', 'price', 'status', 'team']
admin.site.register(chennai, ChennaiAdmin)


class MumbaiAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'role', 'price', 'status', 'team']
admin.site.register(mumbai, MumbaiAdmin)


class DelhiAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'role', 'price', 'status', 'team']
admin.site.register(delhi, DelhiAdmin)


class KolkataAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'role', 'price', 'status', 'team']
admin.site.register(kolkata, KolkataAdmin)


class PunjabAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'role', 'price', 'status', 'team']
admin.site.register(punjab, PunjabAdmin)


class RajasthanAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'role', 'price', 'status', 'team']
admin.site.register(rajasthan, RajasthanAdmin)


class HyderabadAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'role', 'price', 'status', 'team']
admin.site.register(hyderabad, HyderabadAdmin)


class AddTeamAdmin(admin.ModelAdmin):
    list_display = ['TeamImage', 'Team_name', 'HeadLine']
admin.site.register(addTeam, AddTeamAdmin)


class AddNewPlayersAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'role', 'price', 'status', 'team']
admin.site.register( addNewPlayers,AddNewPlayersAdmin)






