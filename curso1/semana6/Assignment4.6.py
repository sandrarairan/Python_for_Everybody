def computepay(h, r):
    if hrs >40:
      pay = (40*r) + (h -40) * r * 1.5
      return pay
    else:
        return(h*r)



hrs = float(input("Enter Hours:"))
rate =float(input("Enter Rate:"))
p = computepay(hrs, rate)
print("Pay", p)