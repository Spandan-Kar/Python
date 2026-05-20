#Low difficulty
numbers= [47, 83, 12, 59, 31,74, 5, 96, 28, 67,3, 88, 41, 62, 15,99, 22, 55, 37, 70, 69, 47, 98, 100]
result= map(
    lambda x: x ** 9,
    numbers
)

print(list(result))

#Medium difficulty
names=[
    "Gyeomi Himejima",
    "Sanemi Shinazugawa",
    "Muichiro Tokito",
    "Genya Shinazugawa",
    "Shinobu Kocho",
    "Giyu Tomioka",
    "Tanjiro Kamado",
    "Zenitsu Agatsuma",
    "Inosuke Hashibira",
    "Tengen Uzui"
]
result= map(
    lambda name: name.upper(),
    names
)
print(list(result))

#High difficulty
employees = [
    {"name": "Spandan Kar", "salary": 150000},  # Lead Developer / Corps Strategist
    {"name": "Giyu Tomioka", "salary": 95000},   # Water Hashira
    {"name": "Mitsuri Kanroji", "salary": 90000}, # Love Hashira
    {"name": "Obanai Iguro", "salary": 92000},    # Serpent Hashira
    {"name": "Sanemi Shinazugawa", "salary": 98000}, # Wind Hashira
    {"name": "Gyomei Himejima", "salary": 110000}, # Stone Hashira (Seniority bonus)
    {"name": "Kyojuro Rengoku", "salary": 100000}, # Flame Hashira
    {"name": "Tengen Uzui", "salary": 105000},    # Sound Hashira (Flamboyant expenses included)
    {"name": "Muichiro Tokito", "salary": 85000},  # Mist Hashira
    {"name": "Shinobu Kocho", "salary": 95000}     # Insect Hashira (Medical division head)
]

#We have to add bonus to their salary
result= [emp["salary"]+50000 for emp in employees] #one way without using map
print(list(result))

result= map(
    lambda emp: {
        "name": emp["name"],
        "salary": emp["salary"]+50000
    },
    employees
)

print(list(result))