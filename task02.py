def atm_operation(balance: int, action: str, amount: int) -> int:
    if amount < 0:
        return "Error: manfiy summa kiritish mumkin emas."
    elif action == 'deposit':
        return balance + amount
    elif action == "withdraw":
        if balance >= amount:
            return balance - amount
        else:
            return "Error: balans yetarli emas."
        
print(atm_operation(100000, 'deposit', 50000))
print(atm_operation(100000, 'withdraw', 200000))
print(atm_operation(100000, 'withdraw', 20000))
print(atm_operation(100000, 'deposit', -1000))