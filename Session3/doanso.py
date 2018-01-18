from random import randint

x = randint(0, 100)

while True:
    y = int(input("Nhap so ban doan 1-100: "))
    if y > x:
        print ("Qua lon")
    elif y < x:
        print ("Qua nho")
    else:
        print("Ban da dung")

    if y == x:
        break

# hoac
# loop = True
#  while loop:
#      y = int(input("Nhap so ban doan 1-100: "))
#      if y == x:
#          print ("Ban da dung")
#          loop = False
#      elif y < x:
#          print ("Qua nho")
#      else:
#          print("Qua lon")
