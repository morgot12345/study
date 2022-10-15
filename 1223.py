def distance(file='test1.txt'):
    with open(file) as input_data:
        return (72 - 60)*int(input_data.read())


print(distance())