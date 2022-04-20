from HudlProject.Credentials.Users import Users


# path will be a local location where username and password will be stored in a document(credentials)

class InvalidCredentials:
    with open(Users.path_2, 'r') as file:
        InvalidCredentials = file.readlines()
        email = InvalidCredentials[0]
        password = InvalidCredentials[1]
