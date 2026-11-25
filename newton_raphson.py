import sympy as sp

# 1. تعريف المتغير x
x = sp.Symbol('x')

# 2. إدخال المعادلة وقيمة X0 من المستخدم
eq_input = input("اكتب المعادلة بدلالة x (مثال: x**3 - x - 2): ")
x0 = float(input("ادخل القيمة الابتدائية X0: "))
max_iter = int(input("ادخل أقصى عدد للخطوات (مثلاً 5): "))

# حساب المشتقة الأولى والثانية تلقائياً
f_expr = sp.sympify(eq_input)
f_prime_expr = sp.diff(f_expr, x)
f_double_prime_expr = sp.diff(f_prime_expr, x)

# تحويل الدوال لتعويض الأرقام
f = sp.lambdify(x, f_expr, 'math')
f_prime = sp.lambdify(x, f_prime_expr, 'math')
f_double_prime = sp.lambdify(x, f_double_prime_expr, 'math')

print(f"\nالدالة: f(x) = {f_expr}")
print(f"المشتقة الأولى: f'(x) = {f_prime_expr}")
print("-" * 55)

# 3. التحقق من شرط التقارب عند X0
try:
    conv_val = abs((f(x0) * f_double_prime(x0)) / (f_prime(x0) ** 2))
    print(f"شرط التقارب عند X0: |f(x0)*f''(x0) / [f'(x0)]^2| = {conv_val:.4f}")
    if conv_val >= 1:
        print("⚠️ تحذير: القيمة >= 1، قد لا تتقارب الطريقة للحل من هذه النقطة.")
except ZeroDivisionError:
    print("❌ خطأ: المشتقة تساوي صفر عند X0.")

print("-" * 55)

# 4. خطوات الانتقال X0 -> X1 -> X2 -> X3 ...
xi = x0
tol = 1e-6

for i in range(max_iter):
    fx = f(xi)
    fpx = f_prime(xi)

    if fpx == 0:
        print(f"توقف عند X{i} لأن المشتقة تساوي صفر.")
        break

    x_next = xi - (fx / fpx)
    print(f"X{i} = {xi:.6f}   --->   X{i+1} = {x_next:.6f}")

    if abs(x_next - xi) < tol:
        print("-" * 55)
        print(f"✅ الحل النهائي التقريبي: {x_next:.6f} (عند X{i+1})")
        break

    xi = x_next
