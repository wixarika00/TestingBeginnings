it = 10

while it > 1:
    if it == 9:
        it = it - 1
        continue  # contunue keyword comes back to lines above it
    if it == 3:
        break
    print(it)
    it = it - 1

print("while loop execution is done")
