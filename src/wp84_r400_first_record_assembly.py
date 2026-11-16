#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec=50

pair=Decimal("0.266329")
cmatch=Decimal("2.1728342265")
R=Decimal(400)
Erec=Decimal("0.163249981456072")

quartic=Decimal(1)/Decimal(2000) + Decimal(213)/Decimal(3000) + Decimal(593)/Decimal(2000)*pair
band=cmatch/R
defect=quartic+band
margin=Erec-defect
simple=Decimal(1)-Decimal(2)*defect

assert defect < Erec
assert margin > Decimal("0.00735")
assert simple > Decimal("0.68820")

print("quartic upper =",quartic)
print("band charge   =",band)
print("defect upper  =",defect)
print("record margin =",margin)
print("simple lower  =",simple)
print("RESULT: WP84_R400_FIRST_RECORD_ASSEMBLY_PASS")
