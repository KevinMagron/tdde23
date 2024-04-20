def check_pnr(person_list):
    product = []
    for i in range(len(person_list)-1):
        if i % 2 == 0:
            product.append(person_list[i] * 2)
        else:
            product.append(person_list[i] * 1)

    sum = 0
    for elem in product:
        if elem > 10:
            sum += elem % 10
            sum += 1
        else:
            sum += elem

    closest_higher_ten = sum + (10 - (sum % 10)) 

    if sum % 10 == 0:
        closest_higher_ten = sum

    control_nbr = closest_higher_ten - sum

    return control_nbr == person_list[-1]
    