import json

class_list = {}

index = int(input('kac kisi kaydedeceksiniz: '))
i = 1


while i <= index:
    name = input(f'{i} Name: ')
    surname = input(f'{i} Surname: ')
    no = input(f'{i} No: ')
    class_list[i] = {
        'Name': name,
        'Surname': surname,
        'No': no
    }
    i += 1
    print(class_list)


for a in class_list[i]:
    print(a)

with open("/home/resul/task.json", "w+") as f:
    json.dump(class_list, f)

print(type(class_list))

#
# class myClass():
#     def __init__(self, index, stu_No, stu_Name, stu_Surname):
#         self.index = index
#         self.stu_No = stu_No
#         self.stu_Name = stu_Name
#         self.stu_Surname = stu_Surname
#
#
#     def print(self):
#         print(myClass.value)
#
#
#
#     def set_stu(self):
#
#         class_list = {}
#         a = int(input('Kac kisi kayit edeceksiniz: '))
#         i = 1
#
#
#         while i <= a:
#             name = input(f'{i} Name: ')
#             surname = input(f'{i} Surname: ')
#             no = input(f'{i} No: ')
#             class_list[i] = {
#                 'Name': name,
#                 'Surname': surname,
#                 'No': no
#             }
#             i += 1
#             print(class_list)


#
#
# myClass.set_stu()
#
#
#
# # stu = myClass(1, 453, 'resul', 'ozdemir')
# #
# #
# #
# # print(stu.index, stu.stu_No, stu.stu_Name, stu.stu_Surname)
# # print(stu.stu_No)
# # print(stu.stu_Name)
# # print(stu.stu_Surname)