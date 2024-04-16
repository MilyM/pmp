# author: Milosz Cygan

# data
data_1 = range(10)

data_2 = [[1,2,4],
          [4,5,6]]

data_3 = {'d1': [1,2,5],
          'd2': (1,5,6),
          'd3': ['abv', 'dd', 123]}

data_4 = range(10, 0, -1)

# loops
for each in data_1:
    print(each)

for iteration, element in enumerate(data_2):
    print(f'Iteration {iteration + 1}, data: {element}')

for elem1, elem2 in zip(data_1, data_4):
    print(f'Element 1: {elem1}, Element 2: {elem2}')


for key, value in data_3.items():
    for each in value:
        print(key, each)