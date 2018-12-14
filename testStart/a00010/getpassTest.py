import getpass

def svc_login(user, passwd):
    if user == 'admin' and passwd == '123456':
        print("hello")
        return True
    elif user != 'admin':
        print('user error')
        return False
    else:
        print('passwd error')
        return False



if __name__ == '__main__':

    # user = getpass.getuser()
    user = input('Enter your username: ')
    passwd = input('Enter your passwd: ')
    # passwd = getpass.getpass()

    if svc_login(user, passwd):    # You must write svc_login()
        print('Yay!')
    else:
        print('Boo!')

