def check_phone_number(number):
    print (number)
    count = 0
    return_number = ""
    for i in range(len(number)):
        print(number[i])
        if(number[i].isnumeric()):
            count += 1
            return_number += number[i]
    print(return_number)
    if(count == 10):
        return return_number
    else:
        return ""

