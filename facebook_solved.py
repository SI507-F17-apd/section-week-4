class Profile:
    def __init__(self, data):
        self.id = data['id']
        self.about = data.get('about')
        self.profile_pic = data.get('profile_pic')

        # NOTE 1
        # I like to use of dict.get(<KEY>, <DEFAULT VALUE (OPTIONAL)>)
        # as it prevents problems, when you are SURE you will
        # NOT ALWAYS get all the key values that you expect

        # NOTE 2
        # how can we make this less repetitive?
        # loop through what keys' values do you want
        # set the key as the attribute of self
        # with the value obtained from the data dictionary

        # for key in ('about', 'profile_pic'):
        #     setattr(self, key, data.get(key))

    def get_posts(self, start=0, limit=10, new=False):
        print('fetching posts from {0} to {1}'.format(start, start + limit - 1))
        # code to fetch posts from database
        # returns a list of Post objects

class User(Profile):
    def __init__(self, data):
        super().__init__(data)
        self.name = data.get('name')
        self.bio = data.get('bio')
        self.birthday = data.get('birthday')
        self.email = data.get('email')
        self.gender = data.get('gender')
        self.hometown = data.get('hometown')

        # NOTE a nicer way to write this
        # for key in ['name', 'birthday', 'email', 'gender', 'hometown']:
        #     setattr(self, key, data.get(key))

    def get_friends_list(self):
        print('fetching friends list for {0}'.format(self.first_name))
        # code to fetch friends list from database
        # returns a list of User objects

class Page(Profile):
    def __init__(self, data):
        super().__init__(data)
        self.featured_video = data.get('featured_video')
        self.groups = self.get_groups_list(data.get('groups', []))
        self.followers = self.get_followers_list(data.get('followers', []))

    def get_groups_list(self, groups_list_of_dicts):
        pass

    def get_followers_list(self, followers_list_of_dicts):
        pass

    def set_featured_video(self, video_id):
        pass


class Group(Profile):
    pass


class Event(Profile):
    pass


class Post:
    def __init__(self, post_data):
        self.id = post_data['id']
        self.post_type = post_data.get('post_type', 'Post')
        self.likes = post_data.get('likes')
        self.content = post_data.get('content')
        self.url = post_data.get('url')

        self.comments = self.get_comments_list(post_data.get('comments', []))
        self.mentions = self.get_mentions_list(post_data.get('mentions', []))

    def like(self):
        self.like += 1
        # QUESTION is this the correct way to do this?

    def unlike(self):
        self.like -= 1
        # QUESTION is this the correct way to do this?

    def new_comment(self, comment_data):
        comment = Comment(comment_data)
        self.comments.append(comment)


class Photo(Post):
    def __init__(self, photo_data):
        super().__init__(photo_data)
        self.location = photo_data.get('location')
        self.people = self.get_people_list(photo_data.get('people'))

    def get_people_list(self, people_list_of_dict):
        people_list = []
        for people_dict in people_list_of_dict:
            pass
            # Create list of User objects and append to people_list_of_dict

class Video(Post):
    def __init__(self, video_data):
        super().__init__(video_data)
        self.resolution = video_data.get('resolution')
        self.source = video_data.get('source')
        self.tags = video_data.get('tags')


# write classes above
# -----------------------------------------------------------------------------
# create objects below

user1_data = {
    "name": "Jane Doe",
    "birthday": "1990/01/01",
    "about": "Hmmm — Just Google my name.",
    "email": "janedoe@example.com",
    "hometown": "Ann Arbor",
}
user1 = User(user1_data)
print(user1.name)
