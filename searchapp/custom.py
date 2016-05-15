from django.conf import settings
import os
# Custom functions
def wrapper(instance, filename):
    path  = os.path.join(settings.MEDIA_ROOT, 'papers/')
    print instance
    print filename
    filename = str(instance.identify) + ".pdf"
    print instance.pk
    print filename
    return os.path.join(path, filename)

def path_and_rename():
    return wrapper 