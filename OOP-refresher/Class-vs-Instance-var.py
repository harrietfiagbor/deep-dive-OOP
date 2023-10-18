class User:
    # class variables
    active_users = []

    def __init__(self, name, email):
        # instance variables
        self.name = name
        self.email = email

    def activate(self):
        if self not in self.__class__.active_users:
            self.__class__.active_users.append(self)

    def deactivate(self):
        if self in self.__class__.active_users:
            self.__class__.active_users.remove(self)

    def is_active(self):
        return self in self.__class__.active_users


person = User("Harriet", "harrietfiagbor@gmail.com")
person.name = "Harriet Fiagbor"
print(person.name)

print(f"Active users: {User.active_users}")
person.activate()
# second activate just to make sure it doesn't activate twice
person.activate()
print(f"Active: {person.is_active()} Active Users: {User.active_users}")
# remove user
person.deactivate()
print(f"Active: {person.is_active()} Active Users: {User.active_users}")
