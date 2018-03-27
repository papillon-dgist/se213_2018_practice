def vat(price, vat_ratio):
    return round(price*vat_ratio/100.0,2)

def tip(price, vat_ratio, tip_ratio, after_tax):
    if(after_tax):
        return round((price+price*vat_ratio/100.0)*tip_ratio/100,2)
    else:
        return round(price*tip_ratio/100.0,2)

def total(price, vat_ratio, tip_ratio, after_tax):
    return round(price+vat(price, vat_ratio)+tip(price, vat_ratio, tip_ratio, after_tax),2)

print(vat(20, 6))
print(vat(12.34, 5))
print(tip(20, 6, 20, False))
print(total(20, 6, 20, False))
print(total(20, 6, 20, True))