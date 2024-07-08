class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post)

    def follow(self, user):
        if user not in self.following:
            self.following.append(user)

    def get_timeline(self):
        timeline = []
        for user in self.following:
            timeline.extend(user.posts)
        timeline.sort(key=lambda x: x.created_at, reverse=True)
        return timeline

    def __repr__(self):
        return f'<User: "{self.first_name} {self.last_name}">'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
