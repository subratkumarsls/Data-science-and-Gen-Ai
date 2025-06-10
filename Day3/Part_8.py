is_member = True
bill_amount = 1200
if is_member:
    if bill_amount>=1000:
        print("Gold discount")
    else:
        print("Regiular discount")
else:
    print("No discount")