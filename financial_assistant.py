def financial_assistant():

    budget = float(input("Enter your budget: ")) # User input for budget

    # Error handling to ensure budget is not less than 0
    while budget < 0:
        print("Budget cannot be less than 0.")
        budget = float(input("Enter your budget: "))

    print(f"Your budget is {budget}") # Display budget

    expenditures = {} # Dictionary to store expenditures
    total_spent = 0 # Variable to track total spent

