from django.apps import AppConfig
 
 
class SearchappConfig(AppConfig):
    name = 'searchapp'
    verbose_name = 'Searchapp Paper Upload Application'
 
    def ready(self):
        import searchapp.signals