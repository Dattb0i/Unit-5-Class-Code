def calculate_total_cost(meal,tip=15):
    total_cost = meal*(1+(tip/100))
    print(f"The total cost of the meal is {total_cost: .2f}")
    
while True:
    try:    
        meal = float(input("Enter the meal cost: "))
        tip = int(input("Enter the tip percentage: "))
    except ValueError:
        print("Invalid input, put in an integer next time.")
        continue
    
    if tip <= 0:
        print("Invalid tip percentage, using default value of 15%.")
        calculate_total_cost(meal,)
        
    if tip > 0:
        calculate_total_cost(meal,tip)
    break

