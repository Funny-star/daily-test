# 约瑟夫问题

def build_list(num_1):
    '''
    创建初始人群
    '''
    person_list = []
    for i in range(1, num_1+1):
        person_list.append(i)
    return person_list


def kill_progress(person_list, num_2):
    '''
    杀人过程
    '''
    while len(person_list) > num_2:
        person_list = person_list[3:len(
            person_list)+1] + [person_list[0], person_list[1]]
    return person_list


num_1 = int(input('总人数：'))
num_2 = int(input('存活人数：'))

print(kill_progress(build_list(num_1), num_2))
