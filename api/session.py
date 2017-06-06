class Session:
    def __init__(self, id, language, cookie):
        self.id = id
        self.language = language
        self.cookie = cookie
        self.password = self.get_password()



    def get_password(self):
        return '12345'