def age_group(age):
    if age <= 12:
        return 'childhood'
    elif age <= 18:
        return 'adolescent'
    elif age <= 65:
        return 'adult'
    else:
        return 'aged'
    
    # the following line will not be executed
    print('The last line of age_group()')

print(age_group(42))