retirement_age = 65
emi_perct = 0.40   # taking 40% of salary for EMI

while True:
    print("\n---------- LOAN ELIGIBILITY SYSTEM ----------")
    print("1. Check Loan Eligibility")
    print("2. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter Applicant Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Monthly Salary (₹): "))
        loan = float(input("Enter Loan Amount (₹): "))

        if age < 21 and age >= retirement_age:
            print("\nLoan Rejected!")
            print("Reason: Age should be between 21 yrs to retirement age.")
            continue

        remaining_years = retirement_age - age

        monthly_emi = salary * emi_perct

        repayment_capacity = monthly_emi * 12 * remaining_years

        print("\n---------- LOAN REPORT ----------")
        print("Applicant Name      :", name)
        print("Age                 :", age)
        print("Monthly Salary      : ₹", salary)
        print("Remaining Years     :", remaining_years)
        print("40% Salary for EMI  : ₹", monthly_emi)
        print("Loan needed         : ₹", loan)
        print("Repayment Capacity  : ₹", repayment_capacity)

        if loan <= repayment_capacity:
            print("\nLOAN APPROVED")
            print("The applicant can repay the loan.")
        else:
            print("\nLOAN REJECTED")
            print("The applicant cannot repay the loan before retirement.")

    elif choice == 2:
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please try again.")