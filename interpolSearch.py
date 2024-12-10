def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:  # Если остался только один элемент
            if arr[low] == target:
                return low  # Элемент найден
            return -1  # Элемент не найден

        # В расчетах используем формулу интерполяции
        pos = low + int((float(high - low) / (arr[high] - arr[low]) * (target - arr[low])))

        if arr[pos] == target:
            return pos  # Элемент найден
        elif arr[pos] < target:
            low = pos + 1  # Ищем в правой части
        else:
            high = pos - 1  # Ищем в левой части

    return -1  # Если элемент не найден, возвращаем -1

# Пример использования функции
sorted_array = [10, 20, 100, 40, 50,300,30]
target_value = 30
result = interpolation_search(sorted_array, target_value)

if result != -1:
    print(f"Элемент {target_value} найден на индексе {result}.")
else:
    print(f"Элемент {target_value} не найден в массиве.")