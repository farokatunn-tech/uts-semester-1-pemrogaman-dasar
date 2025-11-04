print("soal nomor 1 :")
rows = 5
for i in range(rows * 2):
    print("*", end= " ")
print()
for i in range(rows):
    for j in range(rows - i):
        print("*", end = " ")
    for j in range(i * 2):
        print (" ", end= " ")
    for j in range(rows -i ):
        print("*", end= " ")
    print()


print("soal nomor 2 : ") 
rows = 6
for i in range(rows):
    for j in range(rows - i - 1 ):
        print (" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end= " ")
    print()


print("soal nomor 3 :")
raws = 3
for i in range(1, raws + 1):
    for j in range(i):
        print("*", end= " ")
    print()
for i in range(1, raws + 1):
    for j in range(raws - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end= " ")
    print() 


print("soal nomor 4 :")
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    for j in range((rows - i) * 2):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(rows * 2):
    print("*", end=" ")
print()

print("soal nomor 5 : ")
rows = 5 
for i in range(rows, 0, -1):
    for j in range(rows - i):
            print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

print("soal nomor 6 :")
rows = 3
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("soal nomor 7 :")
for p in range(rows, 0, -1):
    for j in range(rows - p):
        print(" ", end=" ")
    for a in range(p):
        print("*", end=" ")
    print()
for p in range(2, rows + 1):
    for j in range(rows - p):
        print(" ", end=" ")
    for a in range(p):
        print("*", end=" ")
    print() 

print("soal nomor 8 :")
rows  = 5
for i in range(rows):
    print("0", end=" ")
    for j in range(2 * rows ):
        print("*", end=" ")
    print()
for i in range(2 * rows + 1 ):
    print("0", end=" ")
print()

print(" ")
print("soal nomor 9 :")
blocks = 5
for k in range(blocks):
    print("*" * 10)
    print("0")

print(" ")
print("soal nomor 10 :")
rows = 5
for  _ in range(6):
    print("*", end=" ")
print()
print(" ")
for i in range(rows, 1, -1):
    for k in range(i):
        print("*", end=" ")
    print()
for i in range(1, rows + 1):
    for k in range(i):
        print("*", end=" ")
    print()

print("soal nomor 11 :")
rows = 5
cols = 10
print("0" * (cols + 1))
for i in range(rows):
    print("0" + "*" * cols)


print("soal nomor 12:")
rows = 5
cols = 10
print("0" * 10)
print("0")
for i in range(rows):
    print("*" * cols)
    print("0")

print("soal nomor 13 :")
rows = 6
cols = 7
for i in range(rows):
    zeros = i + 1
    stars = cols - zeros
    print("0" * zeros + "*" * stars)

print("soal nomor 14:")
rows = 6
cols = 7
for i in range(rows, 0, -1):
    zeros = 1
    stars = cols - zeros
    print("0" * stars + "*" * stars)

print("soal nomor 15:")    
rows = 6
cols = 7
for i in range(1, rows + 1):
    stars = i
    zeros = cols -stars
    print("0" * zeros + "*" * stars)

print("soal nomor 16:")
rows = 6
cols = 7
for i in range(1, rows + 1):
    stars = 1
    zeros = cols - stars
    print("0" * zeros + "*" * stars)


print("s0al nomor 17:")
rows = 6
cols = 7
for i in range(cols):
    line = ""
    for j in range(cols):
        if j == cols - 1 - i:
            line += "*"
        else:
            line += "0"
    print(line)

print("soal nomor 18:")
rows = 6
cols = 7
for i in range(rows):
    line = ""
    for j in range(cols):
        if j == i:
            line += "*"
        else:
            line += "0"
    print(line)

print("s0al nomor 19:")
rows = 6
cols = 7
for i in range(rows):
    if i == 0 or i == rows -1:
        print("0 * cols")
    else:
        print("0" + "*" * (cols - 2) + "0")


print("soal nomor 20:")
cols = 6
blocks = 2
for i in range(blocks):
    print("0" * cols)
    print("*" * cols)
    print("=" * cols)