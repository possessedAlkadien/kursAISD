def binary_search(arr, left, right, target):
    # Вспомогательная функция для выполнения бинарного поиска
    while left <= right:
      mid = left + (right - left) // 2
      if arr[mid] == target:
        return mid  # Элемент найден
      elif arr[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    return -1  # Элемент не найден

def exponential_search(arr, target):
    # Проверяем, если первый элемент является целевым
    if arr[0] == target:
      return 0  # Элемент найден на индексе 0

    # Находим диапазон для бинарного поиска
    index = 1
    while index < len(arr) and arr[index] <= target:
      index *= 2  # Увеличиваем индекс в 2 раза

    # Выполняем бинарный поиск в найденном диапазоне
    return binary_search(arr, index // 2, min(index, len(arr) - 1), target)

# Пример использования функции
sorted_array = [2, 3, 4, 10, 40, 50, 70, 80]
target_value = 10
result = exponential_search(sorted_array, target_value)

if result != -1:
    print(f"Элемент {target_value} найден на индексе {result}.")
else:
    print(f"Элемент {target_value} не найден в массиве.")