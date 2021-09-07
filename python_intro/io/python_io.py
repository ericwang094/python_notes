with open("./test.txt") as file_object:
    contents = file_object.read()
    print(contents.strip())

with open("./test.txt") as file_content:
    '''
    This will read line by line
    '''
    for line in file_content:
        # print like this will result in extra empty line between lines, so in order to remove that line we can do
        # print(line)
        print(line.strip('\n'))

# read birthday in pi
with open("./pi_one_million.txt") as file_content:
    contents = file_content.read()
    my_birthday = "19900904"
    if my_birthday in contents:
        print("my birthday is in pi")
    else:
        print("my birthday is not in pi")

try:
    with open("./test_fail.txt") as file_object:
        '''
        This will raise error as file not find
        '''
        contents = file_object.read()
        print(contents.strip())
except Exception:
    print("no such file")
