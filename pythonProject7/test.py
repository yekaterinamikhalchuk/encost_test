import json

with open("ptn_test.json", "r") as read_file:
    data = json.load(read_file)
    name_list=[]
    for i in data:
        if i['lock'] == True:
            name_list.append(i)

    name_list = sorted(name_list, key=lambda k: k['displayName'])
    my_keys = ['displayName', 'mail', 'post', 'departmentFullName']
    for item in name_list:
        for x in my_keys:
            print(item[x], end=', ')
        print('\n')
