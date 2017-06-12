import os

def update_filename(instance, filename):
    path = 'pin_images/'

    ext = filename.split('.')[-1]
    format = str(instance.id) + '.' + str(ext)

    return os.path.join(path, format)