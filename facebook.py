class Profile:
    pass


class User(Profile):
    pass


class Post:
    pass


class Photo(Post):
    pass


class Video(Post):
    pass



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
