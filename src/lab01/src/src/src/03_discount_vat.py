price=float(input())
discount=float(input())
vat=float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print('База после скидки: ',f"{base:.2f}")
print('НДС:')
print('Итого к оплате:')``
