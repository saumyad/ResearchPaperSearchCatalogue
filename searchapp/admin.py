from django.contrib import admin
from searchapp.models import Author, Category,  Keyword, Source, Reference, PaperUpload, Paper
from django import forms
from django.conf import settings
import os
from searchapp.custom import path_and_rename
# from searchapp.custom import convert_pdf_to_txt
# from searchapp.custom import getKeywords_alchemy
# from searchapp.custom import getKeywords_termextract
# from searchapp.custom import clean_text
# from searchapp.custom_mfunctions import keyword_addition

# class KeywordInline(admin.TabularInline):
#     model = Keyword
#     extra = 1

# class OReferencesInline(admin.TabularInline):
#     model = OReferences
#     extra = 2

class PaperUploadForm(forms.ModelForm):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    
    #Handle file upload
    def save(self, commit=True, force_insert=False, force_update=False, *args, **kwargs):
        m = super(PaperUploadForm, self).save(commit=False, *args, **kwargs)
        if (m.pk == None):
            if len(PaperUpload.objects.all()) !=0 :
                print "not empty"
                obj = (PaperUpload.objects.latest('id'))
                n = getattr(obj, 'id')
                m.identify = str(int(n) + 1)
            else:
                print "empty"
                m.identify = str(1)
        print m.identify
        if commit:
            m.save()
        print "after saving"
        # print m
        # print "Primary Key of the record saved "
        # print m.pk
        # print m.docfile
        # print request.FILES['docfile']
        # m.save_m2m()
        # if commit:
        #     m.save(update_fields=['document'])
        return m
        
    class Meta:
        exclude = ['']    
        model = PaperUpload

class PaperUploadAdmin(admin.ModelAdmin):
    list_display =  ('id', 'publishedYear')
    fieldsets = [
        ('Upload Paper',  {'fields': ['source', 'docfile']}),
        ('Additional information', {'fields': ['publishedYear'], 'classes': ['collapse']}),
    ]    
    form = PaperUploadForm

admin.site.register(Author)
admin.site.register(Category)
# admin.site.register(Keyword)
admin.site.register(Reference)
admin.site.register(PaperUpload, PaperUploadAdmin)
admin.site.register(Source)
admin.site.register(Paper)


