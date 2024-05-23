import pandas as pd

# Данные в виде вложенного словаря
students_grades = {
    'Кирилл': {'Физика': 5, 'Математика': 4, 'Литература': 5, 'География': 5, 'История': 5},
    'Нина': {'Физика': 5, 'Математика': 4, 'Литература': 5, 'География': 4, 'История': 4},
    'Александр': {'Физика': 3, 'Математика': 3, 'Литература': 4, 'География': 5, 'История': 4},
    'Алексей': {'Физика': 4, 'Математика': 3, 'Литература': 5, 'География': 5, 'История': 5},
    'Анастасия': {'Физика': 5, 'Математика': 3, 'Литература': 3, 'География': 4, 'История': 5},
    'Дмитрий': {'Физика': 3, 'Математика': 4, 'Литература': 5, 'География': 5, 'История': 5},
    'Артем': {'Физика': 5, 'Математика': 4, 'Литература': 3, 'География': 3, 'История': 5},
    'Юля': {'Физика': 4, 'Математика': 5, 'Литература': 4, 'География': 5, 'История': 3},
    'Анна': {'Физика': 5, 'Математика': 3, 'Литература': 4, 'География': 5, 'История': 3},
    'Вика': {'Физика': 4, 'Математика': 5, 'Литература': 3, 'География': 4, 'История': 5}
}

# Преобразование словаря в DataFrame
df = pd.DataFrame(students_grades).T

# Печать DataFrame
print(df)

# Рассчет медианной оценки по каждому ученику
median_grades_students = df.median(axis=1)

# Вывод медианной оценки по каждому ученику
print("\nМедианные оценки по каждому ученику:")
for student, median_grade in median_grades_students.items():
    print(f"{student}: {median_grade:.2f}")

# Рассчет медианной оценки по каждому предмету
median_grades_subjects = df.median()

# Вывод медианной оценки по каждому предмету
print("\nМедианные оценки по предметам:")
for subject, median_grade in median_grades_subjects.items():
    print(f"{subject}: {median_grade:.2f}")

# Рассчет Q1 и Q3 для оценок по математике
q1_math = df['Математика'].quantile(0.25)
q3_math = df['Математика'].quantile(0.75)

# Вывод Q1 и Q3 для оценок по математике
print(f"\nQ1 для оценок по математике: {q1_math:.2f}")
print(f"Q3 для оценок по математике: {q3_math:.2f}")