class User():
    def __init__(self, name, username, branch,  password, email, telephone, id=None):
        self.id = id
        self.name = name
        self.branch = branch
        self.username = username
        self.password = password
        self.email = email
        self.telephone = telephone

def to_obj(req):
    return User(
        id = req["_id"],
        name = req["name"],
        branch = req["branch"],
        username = req["username"],
        password = req["password"],
        email = req["email"],
        telephone = req["telephone"],
    )