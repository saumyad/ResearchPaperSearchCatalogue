import datetime
from haystack import indexes
from searchapp.models import Paper, Author


class PaperIndex(indexes.SearchIndex, indexes.Indexable):
    text      = indexes.CharField(document=True, use_template=True)
    title     = indexes.CharField(model_attr='title')
    document  = indexes.CharField(model_attr='document')
    source    = indexes.CharField(model_attr='source', null=True)
    abstract      = indexes.CharField(model_attr='abstract', null=True)
    publishedYear = indexes.IntegerField(model_attr='publishedYear', null=True)

    def get_model(self):
        return Paper

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter()

class AuthorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Author

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter()
    