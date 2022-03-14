from django.contrib import admin
from .models import Ipldata, Iplmatcheswondata, Iplmatchesplayedvswon, Ipltopeconomicalbowlers, Iplextrarunsconcededperseason

# Register your models here.

#admin model for Ipldata
class IpldataAdmin(admin.ModelAdmin):
    list_display = ('title','year','matches')
    ordering = ('year',)
    search_fields = ('title',)

#admin model for Iplmatcheswondata
class IplmatcheswondataAdmin(admin.ModelAdmin):
    list_display = ('teamname','teamabbr','matcheswon')
    ordering = ('matcheswon',)
    search_fields = ('teamname','teamabbr')

#admin model for Iplmatchesplayedvswon
class IplmatchesplayedvswonAdmin(admin.ModelAdmin):
    list_display = ('teamname','teamabbr','year','matchesplayed','matcheswon')
    ordering = ('year',)
    search_fields = ('teamname','teamabbr','year')

#admin model for Ipltopeconomicalbowlers
class IpltopeconomicalbowlersAdmin(admin.ModelAdmin):
    list_display = ('topeconomybowler','teamname','year','matches','economy')
    ordering = ('year',)
    search_fields = ('topeconomybowler','year')

#admin model for Iplextrarunsconcededperseason
class IplextrarunsconcededperseasonAdmin(admin.ModelAdmin):
    list_display = ('title','year','extras')
    ordering = ('year',)

admin.site.register(Ipldata,IpldataAdmin)
admin.site.register(Iplmatcheswondata,IplmatcheswondataAdmin)
admin.site.register(Iplmatchesplayedvswon,IplmatchesplayedvswonAdmin)
admin.site.register(Ipltopeconomicalbowlers,IpltopeconomicalbowlersAdmin)
admin.site.register(Iplextrarunsconcededperseason,IplextrarunsconcededperseasonAdmin)