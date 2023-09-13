hour = 8
totalhour = 4
hourpay = 100
extra = 200
extrahour = totalhour - hour
totalhourpay = hour * hourpay

if totalhour > 8:
    extrahourpay = extrahour * extra
else:
    extrahourpay = 0

if totalhour < 8:
    totalhourpay = totalhour * hourpay

totalpay = totalhourpay + extrahourpay
print(totalpay)