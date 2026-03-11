


def checkout_time(customers, n):
   
    registers = [0] * n

    for customer_time in customers:
       
        min_time = registers[0]
        min_index = 0 
        
        for i in range(1, n):
            if registers[i] < min_time:
                min_time = registers[i]
                min_index = i
        
        registers[min_index] += customer_time

    return max(registers)


print(checkout_time([8, 5, 10, 2, 6, 3, 4], 3))




