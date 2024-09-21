from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.user = None
        self.timestamp = datetime(2017, 1, 10)

    def set_user(self, user):
        self.user = user

    
class TextPost(Post):  
    def __init__(self, text, timestamp=None):
        super(TextPost,self).__init__(text,timestamp)

    def __str__(self):
        return """@{fn} {ln}: "{text}"\n\t{date}""".format(fn = self.user.first_name,ln = self.user.last_name, text = self.text,date = self.timestamp.strftime("%A, %b %d, %Y"))


class PicturePost(Post): 
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost,self).__init__(text,timestamp)
        self.image_url = image_url
    def __str__(self):
        return """@{fn} {ln}: "{text}"\n\t{url}\n\t{date}""".format(fn = self.user.first_name,ln = self.user.last_name,text = self.text,url = self.image_url,date = self.timestamp.strftime("%A, %b %d, %Y"))

class CheckInPost(Post): 
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost,self).__init__(text,timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return """@{fn} Checked In: "{text}"\n\t{lat}, {long}\n\t{date}""".format(fn = self.user.first_name,ln = self.user.last_name,text = self.text,lat = self.latitude,long = self.longitude,date = self.timestamp.strftime("%A, %b %d, %Y"))