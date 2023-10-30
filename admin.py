from django.contrib import admin
from .models import *
# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Mobile','Message')
admin.site.register(contactus,contactusAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','headlines','slider_dec','slider_picture')
admin.site.register(slider,sliderAdmin)

class newbatchesAdmin(admin.ModelAdmin):
    list_display=('id','name','batch_pic','starting_date')
admin.site.register(newbatches,newbatchesAdmin)

class collegeAdmin(admin.ModelAdmin):
    list_display=('id','college_name','college_picture')
admin.site.register(college,collegeAdmin)

class session_yearAdmin(admin.ModelAdmin):
    list_display=('id','session',)
admin.site.register(session_year,session_yearAdmin)

class batchAdmin(admin.ModelAdmin):
    list_display=('id','batch_name',)
admin.site.register(batch,batchAdmin)

class placementAdmin(admin.ModelAdmin):
    list_display=('id','student_picture','student_name','college','session','batch','company_name','company_logo')
admin.site.register(placement,placementAdmin)

class signupAdmin(admin.ModelAdmin):
    list_display = ('name','email','passwd','mobile','profile','course','pyear','college','batch','status','batchid')
admin.site.register(signup,signupAdmin)


class studentbatchAdmin(admin.ModelAdmin):
    list_display = ('id','batch_name')
admin.site.register(studentbatch,studentbatchAdmin)

class mylecturesAdmin(admin.ModelAdmin):
    list_display = ('id','video_category','video_batch','vlink','thumbnail','video_description','added_date')
admin.site.register(mylectures,mylecturesAdmin)

class batchtimingAdmin(admin.ModelAdmin):
    list_display = ('id','batch','clink','timing','start_date')
admin.site.register(batchtiming,batchtimingAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name','category_picture','category_date')
admin.site.register(category,categoryAdmin)

class enotesAdmin(admin.ModelAdmin):
    list_display = ('id','title','note_pic','pdf_notes','batch','added_date')
admin.site.register(enotes,enotesAdmin)

class mytaskAdmin(admin.ModelAdmin):
    list_display = ('id','taskbatch','title','task_file','added_date')
admin.site.register(mytask,mytaskAdmin)

class submittedtaskAdmin(admin.ModelAdmin):
    list_display = ('id','title','answer_file','tid','userid','marks')

admin.site.register(submittedtask,submittedtaskAdmin)