from django.contrib import admin
from staff.models import Team_Member


#add all the fields of the models you want to see on the django admin panel
#just add the word "Admin" to the model name
class Team_MemberAdmin(admin.ModelAdmin):
    list_display = ('team_member_id', 'name',)

#mention all the models to be viewed on the django admin panel
admin.site.register(Team_Member, Team_MemberAdmin)
