def calculate_tax(salary: int) -> dict:
    tax = 0
    net = 0
    rate = ''

    if salary > 20_000_000:
        tax = (salary / 100) * 25
        net = salary - tax
        rate = '25%'
    elif salary > 10_000_000:
        tax = (salary / 100) * 18
        net = salary - tax
        rate = '18%'
    elif salary > 5_000_000:
        tax = (salary / 100) * 12
        net = salary - tax
        rate = '12%'
    
    dc = {"gross": salary, "tax": tax, "net": net, 'rate': rate}

    return dc

print(calculate_tax(8_000_000))
print(calculate_tax(3_000_000))
print(calculate_tax(20_000_001))
print(calculate_tax(11_934_900))