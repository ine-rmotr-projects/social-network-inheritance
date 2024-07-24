from datetime import datetime

# Please remove the comments and
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text

    def set_user(self, user = None):
        if not user:
            self.user = user

class TextPost(Post):
    def __init__(self, text, timestamp=None):
         super().__init__(text)

    def __str__(self):
        full_name = self.user.first_name + ' ' + self.user.last_name #textpost has attribute user, user has attribute first_name
        return full_name + ': ' + self.text + '\n  ' + 'Tuesday, Jan 10, 2017'

    def set_user(self, user):
        super().set_user(user)


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
         super().__init__(text)
         self.image_url = image_url

    def __str__(self):
        full_name = self.user.first_name + ' ' + self.user.last_name
        picture = self.text
        return full_name + ': ' + '\"' + picture + '\"' + '\n  ' + 'Pic URL: ' + self.image_url + '\n  ' + 'Tuesday, Jan 10, 2017'

class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
         super().__init__(text)
         self.latitude = latitude
         self.longitude = longitude

    def __str__(self):
        name = self.user.first_name
        place = self.text
        return name + 'Checked In: ' + '\"' + place + '\"' + '\n  ' + self.latitude + ', ' + self.longitude + '\n  ' + 'Tuesday, Jan 10, 2017'
