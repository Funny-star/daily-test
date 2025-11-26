# 完成一个记事本，要求如下：
# 1） 显示所有代办事项
# 2） 添加新的代办事项
# 3） 标记事项为“已完成”
# 4） 删除待办事项

import os
import time
import json


unfinished_project = []


def print_unfinished_project(unfinished_project):
    '''
    打印记事本
    '''
    if len(unfinished_project) == 0:
        print('暂无项目')
    for i in range(len(unfinished_project)):
        print(f'{i+1} . {unfinished_project[i]}')


def add_project():
    '''
    添加项目
    '''
    project = input('请输入要添加的项目：')
    if project in unfinished_project or project + '#OVER' in unfinished_project:  # 防止添加重复项目
        print(f"项目 '{project}' 已存在，无法重复添加！")
        return unfinished_project
    else:
        unfinished_project.append(project)
        print(f"项目 '{project}' 添加成功！")
        write_file()
        return unfinished_project


def mark_as_finished():
    '''
    标记已完成的项目
    '''
    which_finished = input('请输入已经完成的项目：')
    for i in range(len(unfinished_project)):
        if unfinished_project[i] == which_finished:
            unfinished_project[i] += '#OVER'
            write_file()
    return unfinished_project


def del_project():
    '''
    删除项目
    '''
    del_one = input('请输入要删除的项目：')
    for i in range(len(unfinished_project)):
        if unfinished_project[i] == del_one or unfinished_project[i] == del_one + '#OVER':
            del unfinished_project[i]
            print(f'以删除项目{del_one}')
            write_file()
            return unfinished_project
    print('无此项目')
    return unfinished_project


def notepad():
    global unfinished_project
    command = input('请输入指令：')
    if command == 'a':
        unfinished_project = add_project()
        return unfinished_project
    if command == 'd':
        unfinished_project = del_project()
        return unfinished_project
    if command == 'm':
        unfinished_project = mark_as_finished()
        return unfinished_project
    return unfinished_project


def read_file():
    global unfinished_project
    try:
        file_path = 'project.json'
        with open(file_path, 'r', encoding='utf-8') as f:
            unfinished_project = json.load(f)
    except FileNotFoundError:
        print('未找到文件')


def write_file():
    try:
        file_path = "project.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(unfinished_project, f, ensure_ascii=False, indent=2)
            print('保存成功')
    except Exception as e:
        print(f'保存失败{e}')


read_file()
while True:

    head_command = input('输入s对记事板进行编辑:')
    print('a:添加项目//d:删除项目//m:标记项目')
    time.sleep(1)

    if head_command == 's':
        os.system('cls')
        unfinished_project = notepad()
        time.sleep(1.5)
        os.system('cls')
        print_unfinished_project(unfinished_project)
        continue
