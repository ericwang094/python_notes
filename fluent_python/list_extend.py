# weird_list = [['_'] * 3] * 3
# print(id(weird_list))
# for _ in weird_list:
#     print(id(_))
#
# weird_list[1][2] = "x"
# print(weird_list)

t:tuple = (1,2,3)
print(id(t))
t += (4, 5)
print(id(t))
print(t)