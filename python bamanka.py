import pandas as pd
import os
df = pd.read_csv('c:/Users/annua/Downloads/student_digital_life.csv')
print("=== ПЕРВЫЕ 5 СТРОК ===")
print(df.head())
print("\n")
print("=== ИНФОРМАЦИЯ О ТАБЛИЦЕ ===")
print(df.info())
print("\n")
print("=== СТАТИСТИКА ПО ЧИСЛОВЫМ СТОЛБЦАМ ===")
print(df.describe())
print("\n")
print("=== НАЗВАНИЯ СТОЛБЦОВ ===")
print(df.columns.tolist())
print("\n")
print("=== КОЛИЧЕСТВО ПРОПУСКОВ В КАЖДОМ СТОЛБЦЕ ===")
print(df.isnull().sum())
print("\n")
print(df['gender'])

# Выбор одного столбца
print("=== СТОЛБЕЦ 'final_exam_score' ===")
print(df['final_exam_score'])
print("\n")
# Выбор нескольких столбцов
print("=== СТОЛБЦЫ 'final_exam_score' и 'smartphone_usage_hours' ===")
print(df[['final_exam_score', 'smartphone_usage_hours']])
print("\n")
# Фильтр: СТУДЕНТЫ, КОТОРЫЕ СПЯТ МЕНЕЕ 5 ЧАСОВ
print("=== СТУДЕНТЫ, КОТОРЫЕ СПЯТ МЕНЕЕ 5 ЧАСОВ ===")
sleep_time = df[df['sleep_hours'] < 5]
print(sleep_time[['student_id', 'age', 'sleep_hours', 'final_exam_score']])
print("\n")
# Фильтр: ДЕВУШКИ С ВЫСОКОЙ МОТИВАЦИЕЙ (> 7)
print("=== ДЕВУШКИ С ВЫСОКОЙ МОТИВАЦИЕЙ (> 7) ===")
motivated_girls = df[(df['gender'] == 'Female') & (df['motivation_level'] > 7)]
print(motivated_girls[['student_id', 'age', 'motivation_level', 'final_exam_score']])
print("\n")
# Сложный фильтр: Студенты, которые МАЛО спят (< 5 часов) И МНОГО в телефоне (> 8 часов)
print("=== Студенты, которые МАЛО спят (< 5 часов) И МНОГО в телефоне (> 8 часов) ===")
filtr = df[(df['sleep_hours'] < 5) & (df['smartphone_usage_hours'] > 8)]
print(filtr[['student_id', 'sleep_hours', 'smartphone_usage_hours', 'final_exam_score']])
print("\n")
print("=== СРЕДНИЙ БАЛЛ ПО ПОЛУ ===")
gender_score = df.groupby('gender')['final_exam_score'].mean().round(2)
print(gender_score)
print("\n")
# Количество студентов по полу
print("=== КОЛИЧЕСТВО СТУДЕНТОВ ПО ПОЛУ ===")
gender_count = df['gender'].value_counts()
print(gender_count)
print("\n")
# Разделяем статус здоровья на список (если там несколько значений через запятую)
print("=== РАЗДЕЛЕНИЕ СТАТУСА ЗДОРОВЬЯ НА СПИСКИ ===")
df['health_list'] = df['mental_health_status'].str.split(',')
print(df[['student_id', 'mental_health_status', 'health_list']].head(10))
print("\n")
# Сначала создадим функцию для статуса здоровья
def parse_health_status(cell):
    if pd.isna(cell):
        return []
    try:
        # Разделяем по запятой и очищаем пробелы
        statuses = [s.strip() for s in str(cell).split(',')]
        return statuses
    except:
        return []

# Применяем функцию
df['health_list'] = df['mental_health_status'].apply(parse_health_status)
print("=== РАЗДЕЛЕНИЕ СТАТУСА ЗДОРОВЬЯ НА СПИСКИ ===")
print(df[['student_id', 'mental_health_status', 'health_list']].head(10))
print("\n")
print("=== ТИПЫ ДАННЫХ ПОСЛЕ ПРЕОБРАЗОВАНИЙ ===")
print(df.dtypes)
print("\n")
# Сохраняем результат для следующего занятия
df.to_csv('movies_processed.csv', index=False)
print("Обработанные данные сохранены в movies_processed.csv")
print("=== ИТОГОВАЯ ТАБЛИЦА (ПЕРВЫЕ 3 СТРОКИ) ===")
print(df[['student_id', 'age', 'gender', 'final_exam_score', 'health_list', 'parent_education_level']].head(3))