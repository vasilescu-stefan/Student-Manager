from django.contrib import admin
from django.shortcuts import render, redirect
from .models import Students,Profesori,Cursuri,Note, Optionale
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class StudAdmin(admin.ModelAdmin):
    list_filter = ("an","grupa", )
    list_display=("pk","nr_matricol","nume", "prenume","telefon","an","specializare","grupa","data_nastere","mama","tata","nationalitatea","cetatenia")

class ProfAdmin(admin.ModelAdmin):
    list_filter = ("grad_didactic", )
    list_display=("id_prof","nume", "prenume","grad_didactic","id_curs",)


class CursuriAdmin(admin.ModelAdmin):
    list_filter = ("an","semestru","credite", )
    list_display=("id_curs","titlu_curs","an","semestru","credite",)
    def change_view(self, request, object_id, form_url='', extra_context=None):
        if request.method == 'POST':
            new_name = request.POST.get('titlu_curs')

            old_name = Cursuri.objects.get(id=object_id).titlu_curs
            id_curs = Cursuri.objects.get(id=object_id).id_curs

            obj=Cursuri.objects.get(id=object_id)
            obj.titlu_curs=new_name
            obj.save()


            if new_name != old_name:

                return render(request,'vizualizare/confirmare_subiect.html',context={
                    'new_name': new_name,
                    'old_name': old_name,
                    "id_curs":id_curs,
                    }
                )
        return super().change_view(request, object_id, form_url, extra_context)
    
    def confirm_subject_relation(self, request, object_id, nume_nou, nume_vechi):
        # if request.method == "POST":
        #     nume_buton= request.POST.get("button_name")
        #     print("Nume buton", nume_buton)
        #     if nume_buton == "No":
        #         students = Students.objects.filter(an=nume_vechi.an)
        #         note_objects = Note.objects.filter(nr_matricol__in=students.values_list('nr_matricol', flat=True), id_curs__id_curs=nume_vechi)
        #         print("Student", students)
        #         note_objects.delete()
        #         return redirect("admin/")
        # else:
        return render(request,'vizualizare/confirmare_subiect.html',context={
                    'nume_nou': nume_nou,
                    'nume_vechi': nume_vechi,

                    }
                )

    def save_model(self, request, obj, form, change):
        if change:
            new_name = form.cleaned_data.get('titlu_curs')
            obj.titlu_curs = new_name 
        obj.save()

    def response_change(self, request, obj):
        print("in response_change")
        if request.method == 'POST' and 'No' in request.POST:
            id_curs_nou=obj.id_curs
            an_curs=obj.an
            note_pt_stergere=Note.objects.filter(id_curs=id_curs_nou, an=an_curs, credite__lt=an_curs*60)
            note_pt_stergere.delete()
            
        
        return super().response_change(request, obj)

class NoteAdmin(admin.ModelAdmin):
    list_filter = ("id_curs", )
    list_display=("valoare","id_curs","nr_matricol","data_notare",)

class OptionaleAdmin(admin.ModelAdmin):
    list_display = ("nr_matricol", "pachet", "optiunea1", "optiunea2", "optiunea3", "optiunea4",)



admin.site.register(Students, StudAdmin)
admin.site.register(Profesori, ProfAdmin)
admin.site.register(Cursuri, CursuriAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Optionale, OptionaleAdmin)

