class FoodItem:
    def __init__(self, name, calories, protein, carbs, fat):
       
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def calculate_total_nutrition(food_list):
 
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbs
        total_fat += food.fat

    # 输出结果
    print("=== Daily Nutrition Summary ===")
    print(f"Total Calories: {total_calories} kcal")
    print(f"Total Protein: {total_protein} g")
    print(f"Total Carbs: {total_carbs} g")
    print(f"Total Fat: {total_fat} g")

    # 超标警告
    if total_calories > 2500:
        print("WARNING: Calorie intake exceeds recommended limit (2500 kcal)")
    if total_fat > 90:
        print("WARNING: Fat intake exceeds recommended limit (90 g)")

# 示例调用
if __name__ == "__main__":
    breakfast = FoodItem("Oatmeal", 150, 5, 27, 3)
    lunch = FoodItem("Chicken Salad", 400, 35, 10, 15)
    dinner = FoodItem("Pasta", 600, 20, 80, 10)
    snack = FoodItem("Chips", 200, 3, 20, 12)

    daily_food = [breakfast, lunch, dinner, snack]
    calculate_total_nutrition(daily_food)