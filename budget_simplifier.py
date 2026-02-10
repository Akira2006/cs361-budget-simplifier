total_budget = None
categories = {}

def welcome_screen():
    print("Welcome to Budget Simplifier")
    print("This program helps you divide your income into categories")
    print("and avoid overspending.")
    input("Press Enter to continue...")

def main_menu():
    print("\nMain Menu")
    print("1. Enter total budget")
    print("2. Add category")
    print("3. Set category percentage")
    print("4. View budget breakdown")
    print("5. Help")
    print("6. Exit")
    return input("Choose an option: ")

def enter_total_budget():
    global total_budget
    try:
        value = float(input("Enter total budget: "))
        if value <= 0:
            print("Budget must be greater than zero.")
            return
        total_budget = value
        print("Total budget saved.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_category():
    name = input("Enter category name: ").strip()
    if name == "":
        print("Category name cannot be empty.")
        return
    if name in categories:
        print("Category already exists.")
        return
    categories[name] = 0
    print("Category added.")

def set_category_percentage():
    if not categories:
        print("No categories exist.")
        return

    for name in categories:
        print("-", name)

    name = input("Choose category: ")
    if name not in categories:
        print("Category not found.")
        return

    try:
        pct = float(input("Enter percentage: "))
        if pct < 0 or pct > 100:
            print("Percentage must be between 0 and 100.")
            return

        temp_total = sum(categories.values()) - categories[name] + pct
        if temp_total > 100:
            print("Warning: Total percentage cannot exceed 100.")
            return

        categories[name] = pct
        print("Percentage saved.")
    except ValueError:
        print("Invalid number.")

def view_breakdown():
    if total_budget is None:
        print("Please enter a total budget first.")
        return

    total_pct = sum(categories.values())
    print("\nBudget Breakdown")

    for name, pct in categories.items():
        amount = round(total_budget * pct / 100, 2)
        print(f"{name}: {pct}% -> ${amount}")

    if total_pct < 100:
        remaining_pct = 100 - total_pct
        remaining_amt = round(total_budget * remaining_pct / 100, 2)
        print(f"Unassigned: {remaining_pct}% -> ${remaining_amt}")
    elif total_pct == 100:
        print("Budget plan is valid.")
    else:
        print("Warning: Budget exceeds 100%.")

def help_screen():
    print("\nHow to Use Budget Simplifier")
    print("Step 1: Enter total budget")
    print("Step 2: Add categories")
    print("Step 3: Set category percentages")
    print("Step 4: View budget breakdown")
    input("Press Enter to return to menu...")

def run_program():
    welcome_screen()
    while True:
        choice = main_menu()
        if choice == "1":
            enter_total_budget()
        elif choice == "2":
            add_category()
        elif choice == "3":
            set_category_percentage()
        elif choice == "4":
            view_breakdown()
        elif choice == "5":
            help_screen()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

run_program()
