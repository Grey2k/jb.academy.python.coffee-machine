class User:
    # create the class attributes
    n_active = 0
    users = []

    # create the __init__ method
    def __init__(self, active: bool, user_name: str) -> None:
        self.active = active
        self.user_name = user_name

        if active:
            User.n_active += 1

        User.users.append(self)
