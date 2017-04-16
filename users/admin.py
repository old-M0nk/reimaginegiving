from django.contrib import admin
from users.models import *


#add all the fields of the models you want to see on the django admin panel
#just add the word "Admin" to the model name

class DonorAdmin(admin.ModelAdmin):
    list_display = ('donor_id', 'name', 'mobile', 'email', 'transaction_id')


class DonationAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'name', 'donor_id', 'project_id', 'amount', 'date', 'time', 'status')


class EmailAdmin(admin.ModelAdmin):
    list_display = ('email',)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


class User_DetailsAdmin(admin.ModelAdmin):
    list_display = ('username', 'mobile_number', 'pan_number')


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('username',
                    'supported_projects_mobile',
                    'supported_projects_email',
                    'general_mobile',
                    'general_email',
                    'exciting_projects_mobile',
                    'exciting_projects_email')


class Card_DetailsAdmin(admin.ModelAdmin):
    list_display = ('username', 'card_holder')


class Causes_I_Care_AboutAdmin(admin.ModelAdmin):
    list_display = ('username', 'cause')

#mention all the models to be viewed on the django admin panel

admin.site.register(Donor, DonorAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(User_Details, User_DetailsAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Card_Details, Card_DetailsAdmin)
admin.site.register(Causes_I_Care_About, Causes_I_Care_AboutAdmin)
