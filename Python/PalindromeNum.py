def PalindromeNum(num):
    
    list_num = [0] * len(str(num))
    list_num2 = [0] * len(str(num))

    for i in range(len(list_num)):
        list_num[i] = num % 10
        num //= 10

    for i in range(0, len(list_num)):
        list_num2[i] = list_num[-i - 1]

    for i in range(len(list_num)):
        if list_num == list_num2:
            return True
        return False
    
num = int(input("Insira um número: "))

print(PalindromeNum(num))