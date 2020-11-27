from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text=text
        self.user=None
        if timestamp==None:
            self.timestamp=datetime.now()        
        else:
            self.timestamp=timestamp
            

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.text)
    
    def set_user(self, user):
        self.user=user

class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super().__init__(text, timestamp)

    def __str__(self):
        first=getattr(self.user, 'first_name')
        last=getattr(self.user, 'last_name')
        txt=getattr(self, 'text')
        if self.timestamp!=None:
            date_post=getattr(self, 'timestamp').strftime("%A, %b %d, %Y")
            return '@{} {}: "{}"\n\t{}'.format(first, last, txt, date_post)
        else:
            return '@{} {}: "{}"'.format(first, last, txt)



class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super().__init__(text, timestamp)
        self.image_url=image_url
    
    def __str__(self):
        first=getattr(self.user, 'first_name')
        last=getattr(self.user, 'last_name')
        txt=getattr(self, 'text')
        image_u=getattr(self, 'image_url')
        if self.timestamp!=None:
            date_post=getattr(self, 'timestamp').strftime("%A, %b %d, %Y")
            return '@{} {}: "{}"\n\t{}\n\t{}'.format(first, last, txt, image_u, date_post)
        else:
            return '@{} {}: "{}"\n\t{}'.format(first, last, txt, image_u)


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super().__init__(text, timestamp)
        self.latitude=latitude
        self.longitude=longitude
    
    def __str__(self):
        first=getattr(self.user, 'first_name')
        last=getattr(self.user, 'last_name')
        txt=getattr(self, 'text')
        lat=getattr(self, 'latitude')
        longg=getattr(self, 'longitude')
        if self.timestamp!=None:
            date_post=getattr(self, 'timestamp').strftime("%A, %b %d, %Y")
            return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(first, txt, lat, longg, date_post)
        else:    
            return '@{} Checked In: "{}"\n\t{}, {}'.format(first, txt, lat, longg)
