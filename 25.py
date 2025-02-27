comments = {}


class User:
    """
    An authenticated user with ability to leave comments
    """

    def __init__(self, user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def leave_comment(self, user, text, id):
        comments[id] = {user: text}


class Admin(User):
    def __init__(self, user_name, password, email):
        super().__init__(user_name, password, email)

    def delete_comment(self, id):
        try:
            del comments[id]
        except KeyError:
            print("Comment not found")


ahmad = User("ahmad_hr", "123", "ahmad@gmail.com")
ali = Admin("ali_dev", "123", "ali@gmail.com")

# print(ali.__doc__)

ahmad.leave_comment(ahmad.user_name, input("Leave any comment : "), 1001)
ali.leave_comment(ali.user_name, input("Leave any comment : "), 1002)
ali.leave_comment(ali.user_name, input("Leave any comment : "), 1003)

print(comments)

ali.delete_comment(int(input("enter any comment id to delete : ")))
print(comments)
