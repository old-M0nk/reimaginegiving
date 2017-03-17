from django.contrib import admin
from data.models import Cause, Project, NGO, Consultant, Audit, GiveMonthly, GiveOnce

#add all the fields of the models you want to see on the django admin panel
#just add the word "Admin" to the model name
class CauseAdmin(admin.ModelAdmin):
    list_display = ('cause_id', 'name', 'total_amount')
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'title', 'start_date', 'end_date', 'total_amount', 'raised_amount', 'cause', 'ngo_id', 'zip', 'person_of_contact', 'summary', 'team_member_id', 'story', 'thumbnail', 'banner', 'project_page_desc',)
class NGOAdmin(admin.ModelAdmin):
    list_display = ('ngo_id', 'name', 'person_of_contact', 'registration_code', 'address', 'website', 'team_member_id', 'project_page_desc')
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('consultant_id', 'name',)
class AuditAdmin(admin.ModelAdmin):
    list_display = ('audit_id', 'date', 'report_id', 'consultant_id', 'project_id')
class GiveOnceAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'amount', 'tag',)
class GiveMonthlyAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'amount', 'tag',)


#mention all the models to be viewed on the django admin panel
admin.site.register(Cause, CauseAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(NGO, NGOAdmin)
admin.site.register(Consultant, ConsultantAdmin)
admin.site.register(Audit, AuditAdmin)
admin.site.register(GiveOnce, GiveOnceAdmin)
admin.site.register(GiveMonthly, GiveMonthlyAdmin)