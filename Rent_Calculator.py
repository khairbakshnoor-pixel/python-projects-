# RENT CALCULATOR
rent=int(input("Enter the Total Rent Of the Flat    :"))
food=int(input("Enter the Total Amount of foods     :"))
electriciy_units=float(input("Enter the Total Electricity units spend per Month     :"))
rate_per_month=float(input("Enter the The rate Per month        :"))
persons=int(input("Enter the Total members leaving in the Flat      :"))

if persons <= 0:
    print("Number of persons must be greater than zero!")
else:
    
    total_bill=rate_per_month * electriciy_units
    totalAmount=(total_bill+rent + food)/persons
    print(f"Each person will pay    {totalAmount: .2f} RS: ")
