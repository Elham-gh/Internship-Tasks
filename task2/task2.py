array = ['a', 'b', 'c', 'd']
start = int(input('Please enter an integer as the index to start '))
circular_list = [array[(iterate + start) % (len(array))] for iterate in range(len(array))]
print(circular_list)