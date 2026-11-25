time = int(input("enter time(sanie) = "))

rooz = int(time / 86400)
time = time - (rooz * 86400)
saat = int(time / 3600)
time = time - (saat * 3600)
daghighe = int(time / 60)
time = time - (daghighe * 60)
print(rooz, "roz", ":", saat, "saat", ":", daghighe, "daghigheh", ":", time, "sanieh")
