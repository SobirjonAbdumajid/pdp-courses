import pandas as pd
import matplotlib.pyplot as plt

# Ma'lumotlarni o'qish
df = pd.read_csv('titanic.csv')

# 1. Barcha yo'lovchilar soni, erkaklar soni, ayollar soni
passenger_count = len(df)
male_count = len(df[df['Sex'] == 'male'])
female_count = len(df[df['Sex'] == 'female'])
print("Barcha yo'lovchilar soni:", passenger_count)
print("Erkaklar soni:", male_count)
print("Ayollar soni:", female_count)

# 2. Erkaklar va ayollar soniga mos pie chart hosil qilish
gender_counts = [male_count, female_count]
gender_labels = ['Erkaklar', 'Ayollar']
plt.pie(gender_counts, labels=gender_labels, autopct='%1.1f%%')
plt.title('Yo\'lovchilar')
plt.show()

# 3. Titanic kemasiga chiqish biletlari narxining umumiy summasi va bitta bilet narxining o'rtacha qiymati
total_fare = df['Fare'].sum()
average_fare = df['Fare'].mean()
print("Biletlar umumiy summasi:", total_fare)
print("Bitta bilet narxi o'rtachasi:", average_fare)

# 4. 15-40 yosh oralig'idagi yo'lovchilar umumiy yo'lovchilarning necha foizini tashkil etishi
age_15_to_40_count = len(df[(df['Age'] >= 15) & (df['Age'] <= 40)])
percentage_15_to_40 = (age_15_to_40_count / passenger_count) * 100
print("15-40 yosh oralig'idagi yo'lovchilar foizi:", percentage_15_to_40)

# 5. Tirik qolgan bolalar (yoshi 16 dan kichik) barcha bolalarning necha foizini tashkil etishi
child_count = len(df[df['Age'] <= 16])
percentage_children = (child_count / passenger_count) * 100
print("Tirik qolgan bolalar foizi:", percentage_children)