try:
    my_list = []

    while True:
        my_list.append(int(input())) and input() !=0

except:
    my_list=my_list[::-1]
    print(my_list)
