import bisect

grades = [20, 40, 65, 85, 100]
score_labels = [1, 2, 3, 4, 5]

def get_grade(score):
    index = bisect.bisect_right(grades, score)
    return score_labels[index]

# Foydalanuvchidan sonni olish
score = int(input("Iltimos, o'quvchingizning bahosini kiriting (0-100 oralig'ida): "))

# Baho berish
grade = get_grade(score)

# Baho ekranga chiqarish
print(f"O'quvchingizning baho darajasi: {grade}")