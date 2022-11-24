def check_password(data):
    if data["password"] == data["psw_repeat"]:
        return True
    return False
