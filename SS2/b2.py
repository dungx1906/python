print("- BLOOD DONOR SCREENING SYSTEM --- ")
donor_age = int(input("Enter donor's age: ") )
donor_weight = float(input("Enter donor's weight (kg): "))

# Hệ thống kiểm tra diều kiện hiến máu
if (donor_age >= 18 and donor_weight >= 50):
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")