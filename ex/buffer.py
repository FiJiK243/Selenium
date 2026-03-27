import math
import pyperclip

# Пример значения x
x = int(input())  # можно заменить на любое число

# Вычисляем ln(abs(12*sin(x)))
result = math.log(abs(12 * math.sin(x)))

# Копируем результат в буфер обмена
pyperclip.copy(str(result))

print(f"Результат: {result} скопирован в буфер обмена!")
