numbers=[1, 2, 3, 4, 5]
results = []
for n in numbers:
    results.append(n * 2)

print(numbers)
print(results)

results = [(n * 2) for n in numbers]
print(results)