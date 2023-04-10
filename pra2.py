import random

def in_order(num):
    for i in range(len(num)-1):
        if num[i]>num[i+1]:
            return False
    return True

def bogo_sort(num):
    while not in_order(num):
        random.shuffle(num)
    return num


if __name__ == '__main__':
    print(bogo_sort([1,3,2,4]))


#dictionary
d = {"item1": "car", "item2": "bike"}
print("item2" in d)

set = {1,2,2,23,4,5}

set.add(0)
print(set)




array = ['apple', 'banana', 'grape']
array2 = ["good", "yea", "amazing"]

for i, a in enumerate (array):
    print(i)

for a, b in zip(array, array2):
    print(a+b)


dic= {"x":"hey", "y":"oh"}

for k, v in dic.items():
    print(k + v)


def start(a, b):
    print(a + " " + "hey")


start("Oh", "whatever")

def roopKV(**kwargs):
    for k, v in kwargs.items():
        print(k + v)

d = {
    '1':'hey',
    '2':'okay',
    '3':'oh'
    }


roopKV(**d)

print("hey")

print("ex")

