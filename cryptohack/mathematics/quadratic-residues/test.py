p = 29
for i in range(1, 29):
    if i * i % 29 == 14:
        print(str(i) + "(14)")
    elif i * i % 29 == 6:
        print(str(i) + "(6)")
    elif i * i % 29 == 11:
        print(i + "(11)")
