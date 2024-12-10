def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Находим средний индекс
        if arr[mid] == target:
            return mid  # Если элемент найден, возвращаем индекс
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой части
        else:
            right = mid - 1  # Ищем в левой части

    return -1  # Если элемент не найден, возвращаем -1

# Пример использования функции
sorted_array = [1, 2, 5, 5, 6, 9]
target_value = 9
result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Элемент {target_value} найден на индексе {result}.")
else:
    print(f"Элемент {target_value} не найден в массиве.")