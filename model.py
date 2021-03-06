class User(dict):
    """ Every user must have keys for a username, name, password (this
    is a md5 hash of the password), groups, and an email address.  They can be
    blank or None, but the keys must exist. """
    def __init__(self, dict=None):
        for key in ['username', 'name', 'password', 'email']:
            self[key] = ''
        for key in ['groups']:
            self[key] = []
        for key in dict:
            self[key] = dict[key]

    def __getattr__(self, attr):
        return None
