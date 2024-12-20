# Данные: список оценок и множество студентов
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Как работает программа:
# Данные: Имеются два исходных набора данных: grades (список оценок) и students (множество имен студентов).

# Создание пустого словаря для хранения средних баллов
average_grades = {}

# Как работает программа:
# Создание словаря: Создается пустой словарь average_grades, в который будут добавляться имена студентов и их средние баллы.

# Преобразуем множество студентов в список и сортируем по алфавиту
sorted_students = sorted(students)

# Как работает программа:
# Сортировка: Множество students преобразуется в список и сортируется по алфавиту, чтобы соответствовать порядку оценок в списке grades.

# Вычисление среднего балла для каждого студента
for i, student in enumerate(sorted_students):
    if i < len(grades):  # Проверка, чтобы избежать выхода за пределы списка оценок
        average = sum(grades[i]) / len(grades[i])  # Вычисляем среднее значение
        average_grades[student] = average

# Как работает программа:
# Вычисление среднего: Используется цикл for, чтобы пройтись по каждому студенту и его соответствующим оценкам. Средний балл вычисляется с использованием функций sum() и len(). Если количество студентов больше, чем количество списков оценок, то код проверяет, чтобы не выйти за пределы списка grades.

# Вывод результата на экран
print(average_grades)

# Как работает программа:
# Вывод результата: Наконец, словарь с именами студентов и их средними баллами выводится на экран.
