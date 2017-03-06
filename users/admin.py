from django.contrib import admin
from users.models import Donor, Donation, Email, ContactUs


#add all the fields of the models you want to see on the django admin panel
#just add the word "Admin" to the model name

class DonorAdmin(admin.ModelAdmin):
    list_display = ('donor_id', 'name', 'mobile', 'email', 'transaction_id')


class DonationAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'donor_id', 'project_id', 'amount', 'date', 'time')


class EmailAdmin(admin.ModelAdmin):
    list_display = ('email',)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

#mention all the models to be viewed on the django admin panel

admin.site.register(Donor, DonorAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
