fp_number =12345.6789
fp_number2 = 12345612345.6789
fp_number3=.6789
dc_number= 6789
print(f"{fp_number:.2f} ")

print(f"{fp_number:,.2f}")

print(f"{fp_number2:15,.2f}")

##different types of codes
print(f"{fp_number3:.0%}")
print(f"{fp_number3:.1%}")

print(f"{dc_number:d}")

#formatting string literals
print(f"{"description":15}")
print(f"{"description":15}{'price':>10}{'qty':>5}")
