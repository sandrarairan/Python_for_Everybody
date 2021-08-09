hrs =float(input("Enter Hours:"))
rate =float(input("Enter Rate:"))

if hrs >40:
    print((40*rate) + (hrs -40) * rate * 1.5) 
else:
    print(hrs * rate)


