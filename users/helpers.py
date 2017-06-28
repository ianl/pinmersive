import os

def update_filename(instance, filename):
    path = 'user_profile_avatars/'

    ext = filename.split('.')[-1]
    format = str(instance.user.username) + '.' + str(ext)

    return os.path.join(path, format)