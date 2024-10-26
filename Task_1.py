from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Створення задачі лінійного програмування для максимізації
model = LpProblem(name="maximize_drink_production", sense=LpMaximize)

# Змінні для кількості одиниць "Лимонаду" та "Фруктового соку"
lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# Додавання цільової функції (максимізація загальної кількості напоїв)
model += lpSum([lemonade, fruit_juice]), "Total Products"

# Додавання обмежень на ресурси
model += (2 * lemonade + 1 * fruit_juice <= 100), "Water Constraint"       
model += (1 * lemonade <= 50), "Sugar Constraint"                           
model += (1 * lemonade <= 30), "Lemon Juice Constraint"                     
model += (2 * fruit_juice <= 40), "Fruit Puree Constraint"                 

# Розв'язання задачі
model.solve()

# Отримання результатів
lemonade_qty = lemonade.value()
fruit_juice_qty = fruit_juice.value()
total_products = lemonade_qty + fruit_juice_qty

print(f"Максимальна кількість 'Лимонаду': {lemonade_qty}")
print(f"Максимальна кількість 'Фруктового соку': {fruit_juice_qty}")
print(f"Загальна максимальна кількість напоїв: {total_products}")

