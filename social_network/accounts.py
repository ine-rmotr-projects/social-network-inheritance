class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []
        self.timeline = []
        self.followed = []

    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post)
        for user in self.followed:
            if post in user.timeline:
                continue
            else:   
                user.timeline.append(post)

    def get_timeline(self):
        return sorted(self.timeline,key=lambda post: post.timestamp)

    
    def follow(self, other):
        self.following.append(other)
        other.followed.append(self)
        for post in other.posts:
            self.timeline.append(post)