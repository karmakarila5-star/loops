print("=== atm cash dispenser===")
print("dipensing cash for customer one at a time .\n")
notes = [100,50,20,10,5,1]
customer_served = 0
total_dispensed = 0 
log = []
serving = True
while serving:
    name = input("enter customer name:")
    amount = int(input(f"hellow{name}!enter withdrawal amount:"))
    if amount <= 0:
        print("invalid amount. please enter a positive number . \n")
        continue
    print(f"\ndispensind{amount} units for {name}:")
    print("-" * 30)
    remaining = amount
    i = 0
    used = {}
    while i < len(notes):
        count = remaining// notes[i]
        if count > 0:
            print(f" {count} x {notes[i]}-unit note(s) = {count*notes[i]}")
            used[notes[i]] = count
            remaining -= count * notes[i]
            i+= 1
            customer_served += 1
            total_dispended += amount
            log.append({"name": name, "used": used})
            print(f"transaction complete! please collect your cast, {name}. \n")
        
                                                  


