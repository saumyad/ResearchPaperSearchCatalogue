from django.db import models
from django.utils import timezone
from datetime import datetime
from searchapp.custom import path_and_rename
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_save
# Create Models here. Basic ones should be research paper(Paper), (Author), (User)
# Just included a basic template

# (Last edited Sat Nov 29 : dvd)

## Author model
## [TODO] add more attributes
class Author(models.Model):
    name     = models.CharField(('Name'), max_length=60)
    
    def __unicode__(self):
        return self.name

## Category of publication
##
class Category(models.Model):
    categoryName = models.CharField(('Name'), max_length=60)

    def __unicode__(self):
        return self.categoryName

## Sources of publication
class Source(models.Model):
    sourceName = models.CharField(('Source'), max_length=60)

    def __unicode__(self):
        return self.sourceName

## Paper upload field
class PaperUpload(models.Model):
    docfile         = models.FileField(('Upload File'), upload_to=path_and_rename(), null=True, help_text="Browse a file")
    identify        = models.CharField(('Title'), default='Uploaded Paper', max_length = 60)
    YEAR_CHOICES = []
    for r in range(1920, (datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    # timeInsertion   = models.DateTimeField(('Added on'), auto_now=True)
    publishedYear   = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.now().year)
    source          = models.ForeignKey(Source, max_length=60, blank=True)

    def __unicode__(self):
        return self.identify


##References
class Reference(models.Model):
    description    = models.CharField(('References'), max_length=1200)

    def __unicode__(self):
        return self.description


## Keywords associated with paper
class Keyword(models.Model):
    keyword = models.CharField(('Keyword'), max_length=120)
 
    def __unicode__(self):
        return self.keyword

##
## Publication model [TODO] add more constraints
## Add upload field for admins

class Paper(models.Model):
    title           = models.CharField('Title of the paper', max_length=100)
    author          = models.ManyToManyField(Author, blank=True)
    document        = models.TextField(blank=True)
    source          = models.TextField(blank=True, default='ACM Digital Library')
    abstract        = models.TextField(blank=True)
    publishedYear   = models.IntegerField(('year'), default=datetime.now().year)
    timeInsertion   = models.DateTimeField(('Added on'), auto_now=True)
    category        = models.ManyToManyField(Category, blank=True)
    paper_upload    = models.ForeignKey(PaperUpload, blank=True, null=True)
    references      = models.ManyToManyField(Reference, blank=True)
    keywords        = models.ManyToManyField(Keyword, blank=True)
    
    def __unicode__(self):
        return self.title
