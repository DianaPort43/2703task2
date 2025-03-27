from geometry import calculate_area

print("Тест: calculate_area('rectangle', width=4, height=5)")
print("Ожидание: 20, Получено:", calculate_area("rectangle", width=4, height=5))

print("Тест: calculate_area('square', side=4)")
print("Ожидание: 16, Получено:", calculate_area("square", side=4))

print("Тест: calculate_area('circle', radius=3)")
print("Ожидание: ~28.27, Получено:", round(calculate_area("circle", radius=3), 2))