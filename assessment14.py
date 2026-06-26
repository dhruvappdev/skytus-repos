#1. To-Do List CLI
def todo_cli():
    tasks = []
    
    while True:
        print("\n--- 📌 To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print("\n📋 Your Tasks:")
            if not tasks:
                print("List is empty! 🎉")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
                
        elif choice == '2':
            new_task = input("Enter the new task: ")
            tasks.append(new_task)
            print("✅ Task added!")
            
        elif choice == '3':
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"🗑️ Removed: {removed}")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")
                
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

#2. Bank Management System
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        print(f"🏦 Account created for {self.account_holder}.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"💵 Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"💸 Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("❌ Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"💰 Current balance for {self.account_holder}: ${self.balance}")

#3. Quiz Game
def quiz_game():
    questions = {
        "What is the capital of France?": "Paris",
        "What is 5 + 7?": "12",
        "What programming language are we using?": "Python"
    }
    
    score = 0
    print("🎮 Welcome to the Python Quiz Game! 🎮\n")
    
    for question, correct_answer in questions.items():
        print(f"❓ {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == correct_answer.lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {correct_answer}\n")
            
    print(f"🏆 Quiz Complete! You scored {score} out of {len(questions)}.")

#4. Weather App (API)
import requests

def get_weather(city_name, lat, lon):
    print(f"🔍 Fetching weather for {city_name}...")
    
    # Using Open-Meteo free API (no key required)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Check for errors
        data = response.json()
        
        current = data['current_weather']
        temp = current['temperature']
        wind = current['windspeed']
        
        print("\n--- 🌤️ Weather Report ---")
        print(f"📍 City/Location: {city_name}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💨 Wind Speed: {wind} km/h")
        print("-------------------------")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")

#5. Simple E-Commerce Cart System
class ShoppingCart:
    def __init__(self):
        self.cart = {} # Format: {item_name: {'price': 0, 'quantity': 0}}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.cart:
            self.cart[item_name]['quantity'] += quantity
        else:
            self.cart[item_name] = {'price': price, 'quantity': quantity}
        print(f"🛍️ Added {quantity}x {item_name} to cart.")

    def view_cart(self):
        print("\n--- 🛒 Your Shopping Cart ---")
        if not self.cart:
            print("Cart is empty!")
            return
            
        total = 0
        for item, details in self.cart.items():
            cost = details['price'] * details['quantity']
            total += cost
            print(f"🔸 {item}: ${details['price']} x {details['quantity']} = ${cost}")
            
        print("-----------------------------")
        print(f"💳 Total Checkout: ${total}\n")

