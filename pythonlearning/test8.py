try:
    user = input('name')
    if len(user) >= 10:
        raise Exception('错误')
    else:
        print(user)
except Exception as e:
    print(e)


import test7
test7.game()
