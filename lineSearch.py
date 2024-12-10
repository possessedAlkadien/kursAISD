def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

# Пример использования функции
array = [5, 2, 9, 1, 5, 6]
target_value = 10
result = linear_search(array, target_value)

if result != -1:
    print(f"Элемент {target_value} найден на индексе {result}.")
else:
    print(f"Элемент {target_value} не найден в массиве.")