a, b, c = map(int, input().split())
op1 = ""
op2 = ""
if a + b == c:
    op1, op2 = "+", "="
elif a - b == c:
    op1, op2 = "-", "="
elif a * b == c:
    op1, op2 = "*", "="
elif a / b == c:
    op1, op2 = "/", "="
elif a == b + c:
    op1, op2 = "=", "+"
elif a == b - c:
    op1, op2 = "=", "-"
elif a == b * c:
    op1, op2 = "=", "*"
elif a == b / c:
    op1, op2 = "=", "/"

print(str(a) + op1 + str(b) + op2 + str(c))
