
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.list_posts = []
        self.following = []

    def add_post(self, post):
        post.set_user(User)
        self.list_posts.append(post)
        return(self.list_posts)

    def get_timeline(self):
        all_posts = []
        for u in self.following:
            for p in u.list_posts:
                all_posts.append(p)
        return(all_posts)
            
    def follow(self, other):
        if other in self.following:
            self.following.append(other)
        return(self.following)
