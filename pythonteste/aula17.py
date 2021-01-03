num = [2, 5, 9, 1]
num[2] = 3
num.append(1)
num.sort(reverse=True)
print(num)
num.pop(2)
num.insert(3, 10)
print(num)
print(f"Essa lista tem {len(num)} itens!")
