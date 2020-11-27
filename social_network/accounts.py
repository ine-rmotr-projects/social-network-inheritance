class User(object):
    def __repr__(self):
        return '[<User: "{} {}">]'.format(self.first_name, self.last_name)
    
    def __init__(self, first_name, last_name, email):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email

    def add_post(self, post):
        post.set_user(self)
        if hasattr(self, 'posts'):
            self.posts.append(post)
        else:
            self.posts=[]
            self.posts.append(post)
    

    def get_timeline(self):    
        timeline_list=[n for x in self.following if hasattr(x, 'posts')==True for n in x.posts]
        timeline_list.sort(key=lambda x: x.timestamp, reverse=True)
        return timeline_list

    def follow(self, other):
        if hasattr(self, 'following'):
            self.following.append(other)
        else:
            self.following=[]
            self.following.append(other)
