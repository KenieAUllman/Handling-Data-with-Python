open_file = open("CupcakeInvoices.csv")
total = 0.0

for line in open_file:
    #print(line)
    line = line.strip()
    values = line.split(",")
    print(values[2])
    customer_cost = (float(values[3]) * float(values[4]))
    print(customer_cost)
    total += float(customer_cost)
print(f"total customer cost: {total}")




