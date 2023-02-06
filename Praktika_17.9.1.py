array_num = input("Введите числа в любом порядке через пробел: ")
array_num = list(map(int, array_num.split()))


def sort():
    for i in range(len(array_num)):
        for j in range(len(array_num)-i-1):
            if array_num[j] > array_num[j+1]:
                array_num[j], array_num[j+1] = array_num[j+1], array_num[j]
    return array_num


sort()
print(array_num)
number = int(input("Введите любое число: "))


def binary_search(array, element):
    first = 0
    last = len(array)
    while first < last:
        mid = (first+last)//2
        if element > array[mid]:
            first = mid+1
        else:
            last = mid
    return first-1 if 0 < first < len(array) else "Такого числа нет в диапазоне списка"


while number == array_num[0] or number > array_num[-1]:
    print("Ввод не соответствует параметрам")
    number = int(input("Введите любое число: "))


print(binary_search(array_num, number))
