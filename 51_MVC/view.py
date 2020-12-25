import model
from controller import SimpleController

class UserView:
    def __init__(self):
        self.controller = SimpleController(self)

    def create_user(self):
        username = input("Username:")
        mail = input("mail:")
        self.controller.create(username, mail)

    def get_user(self):
        user_id = input ("User id:")
        self.controller.get(user_id)

    def update_display(self, bol, msg):
        if isinstance(msg,model.User):
            msg = f"{msg.username},{msg.email}"
        if bol:
            print (f">> Success", msg)
        else:
            print (f">> Failure", msg)
