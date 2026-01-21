# 1.1 Foydalanuvchidan ismini so'rab, salom beruvchi dastur
# ==================================================
name = input("Ismingizni kiriting: ")
print("Salom,", name)



# ==================================================
# 1.3 Ikki sonning arifmetik amallari
# ==================================================
a = float(input("1-son: "))
b = float(input("2-son: "))

print("Yig'indi:", a + b)
print("Ayirma:", a - b)
print("Ko'paytma:", a * b)
print("Bo'linma:", a / b)

# ==================================================
# 1.4 Temperatura konvertori
# ==================================================
c = float(input("Celsius: "))
f = c * 9/5 + 32
print("Fahrenheit:", f)

# ==================================================
# 1.5 Uchburchak gipotenuzasi
# ==================================================
import math

a = float(input("a: "))
b = float(input("b: "))
c = math.sqrt(a*a + b*b)
print("Gipotenuza:", c)


# ==================================================
# 1.6 Son juft yoki toq
# ==================================================
n = int(input("Son: "))

if n % 2 == 0:
    print("Juft")
else:
    print("Toq")

# ==================================================
# 1.7 Son musbat, manfiy yoki nol
# ==================================================
n = float(input("Son: "))

if n > 0:
    print("Musbat")
elif n < 0:
    print("Manfiy")
else:
    print("Nol")

# ==================================================
# 1.8 3 ta sondan eng kattasi
# ==================================================
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print("Eng kattasi:", max(a, b, c))

# ==================================================
# 1.9 Sekund → soat:daqiqa:soniya
# ==================================================
sec = int(input("Sekund: "))

soat = sec // 3600
daqiqa = (sec % 3600) // 60
soniya = sec % 60

print(soat, ":", daqiqa, ":", soniya)

# ==================================================
# 1.10 2, 3, 5 ga bo'linishini tekshirish
# ==================================================
n = int(input("Son: "))

if n % 2 == 0:
    print("2 ga bo'linadi")
if n % 3 == 0:
    print("3 ga bo'linadi")
if n % 5 == 0:
    print("5 ga bo'linadi")

# ==================================================
# 1.11 Son raqamlari yig'indisi
# ==================================================
n = input("Son: ")
s = 0

for i in n:
    s += int(i)

print("Yig'indi:", s)

# ==================================================
# 1.12 Sonni teskari chiqarish
# ==================================================
n = input("Son: ")
print("Teskari:", n[::-1])


# ==================================================
# 1.13 Kvadrat tenglama
# ==================================================
import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b*b - 4*a*c

if d < 0:
    print("Ildiz yo'q")
elif d == 0:
    x = -b / (2*a)
    print("Bitta ildiz:", x)
else:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Ildizlar:", x1, x2)

# ==================================================
# 1.14 Kg ↔ funt
# ==================================================
kg = float(input("Kg: "))
print("Funt:", kg * 2.20462)


# ==================================================
# 1.15 Bank foiz (5 yil)
# ==================================================
p = float(input("Pul: "))
r = float(input("Foiz (%): "))

for i in range(5):
    p += p * r / 100

print("5 yildan keyin:", p)

# ==================================================
# 1.16 Uch xonali son raqamlari
# ==================================================
n = int(input("Son: "))

yuz = n // 100
on = (n // 10) % 10
bir = n % 10



# ==================================================
# 1.17 Soat → minut
# ==================================================
soat = int(input("Soat: "))
print("Minut:", soat * 60)

# ==================================================
# 1.18 O'rtacha qiymat
# ==================================================
a = float(input())
b = float(input())
c = float(input())

print("O'rtacha:", (a + b + c) / 3)

# ==================================================
# 1.19 1 dan N gacha yig'indi
# ==================================================
n = int(input("N: "))
print("Yig'indi:", n*(n+1)//2)


# ==================================================
# 1.20 4 ta sondan juftlari
# ==================================================
nums = [int(input()) for _ in range(4)]

for n in nums:
    if n % 2 == 0:
        print(n)

# ==================================================
# 1.21 Kvadrat va kub
# ==================================================
n = float(input("Son: "))
print("Kvadrat:", n*n)
print("Kub:", n**3)

# ==================================================
# 1.22 Talabaning o'rtacha bahosi
# ==================================================
a = float(input())
b = float(input())
c = float(input())

print("O'rtacha:", (a + b + c) / 3)

# ==================================================
# 1.23 Doira uzunligi
# ==================================================
pi = 3.14159
r = float(input("Radius: "))
print("Uzunlik:", 2 * pi * r)

# ==================================================
# 1.24 Masofa (s = vt + at²/2)
# ==================================================
v = float(input("Tezlik: "))
a = float(input("Tezlanish: "))
t = float(input("Vaqt: "))

s = v*t + (a*t*t)/2
print("Masofa:", s)


# ==================================================
# 1.25 To'g'ri to'rtburchak
# ==================================================
a = float(input("a: "))
b = float(input("b: "))

print("Perimetr:", 2*(a+b))
print("Yuzi:", a*b)

# ==================================================
# 1.26 N sekunddan keyin soat
# ==================================================
n = int(input("Sekund: "))
print("Soat:", (n//3600)%24)


# ==================================================
# 1.27 2 xonali sonni solishtirish
# ==================================================
n = input("Son: ")
print(n == n[::-1])

# ==================================================
# 1.28 4 ga karrali
# ==================================================
n = int(input("Son: "))
print(n % 4 == 0)

# ==================================================
# 1.29 3 xonali o'sish tartibi
# ==================================================
n = input("Son: ")
print(n[0] < n[1] < n[2])

# ==================================================
# 1.30 Ikki vaqt oralig'i
# ==================================================
h1, m1 = map(int, input("1-vaqt (h m): ").split())
h2, m2 = map(int, input("2-vaqt (h m): ").split())

t1 = h1*60 + m1
t2 = h2*60 + m2

print("Farq (minut):", abs(t2 - t1))