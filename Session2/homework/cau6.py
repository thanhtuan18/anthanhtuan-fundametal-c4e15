n = int(input("dien n cho cong thuc '1*2*3*...*n' "))

for i in range(0, n-1):
    n = n * (i+1)

print("Ket qua cong thuc '1*2*3*...*n' la: ", n)
