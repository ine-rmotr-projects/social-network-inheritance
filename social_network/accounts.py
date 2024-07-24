
class User(object):
    posts = []
    following = []
    timeline = []

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post.text)
        if self in user.following:
            user.following.insert(0, post.text)

    def get_timeline(self):
        full_name = user.first_name + ' ' + user.last_name

    def follow(self, other):
        other_name = other.first_name + ' ' + other.last_name
        followers = ['<User: ' + '\"' + '{name}'.format(name = other_name) + '\">']
        return self.following.append(followers)
