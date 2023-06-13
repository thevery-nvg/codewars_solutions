
'''https://www.codewars.com/kata/55e4c52ad58df7509c00007e/train/python'''


def validate(username, password):
    if '||' in password or '//'in password:return "Wrong username or password!"
    database = Database()
    return database.login(username,password)
