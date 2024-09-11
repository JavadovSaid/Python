def credit_validation(credit_number):
    credit_number = ''.join(filter(str.isdigit, credit_number))
    sum_odd_digit = 0
    sum_even_digit = 0
    credit_number =credit_number[::-1]
    for index,digit in enumerate(credit_number):
        num = int(digit)
        if index%2 ==0:
            sum_even_digit+=num
        else:
            num = num*2
            if num>9:
                num-=9
            sum_odd_digit+=num
    total = sum_odd_digit+sum_even_digit
    if total %10 ==0:
        return 'Valid'
    else:
        return 'Invalid'
user_input = input("Enter: ")
result = credit_validation(user_input)
print(result)







