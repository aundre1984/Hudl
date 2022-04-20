from HudlProject.Credentials.Users import Users


# path will be a local location where username and password will be stored in a document(credentials)

class Credentials:
    with open(Users.path, 'r') as file:
        credentials = file.readlines()
        email = credentials[0]
        password = credentials[1]
