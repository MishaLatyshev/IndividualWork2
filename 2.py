leg1 = float(input("Введите длину первого катета:"))
leg2 = float(input("Введите длину второго катета:"))
hypotenuse = (leg1**2 + leg2**2)**(1/2)
area = (leg1 * leg2)*(1/2)
perimeter = leg1 + leg2 + hypotenuse

print("Area of this triangle is:",area)
print("Perimeter of this triangle is:",perimeter)
