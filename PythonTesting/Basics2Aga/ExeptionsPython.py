ItemsInCart = 0
# 2 items will be dded to cart
if ItemsInCart !=2:  # raise Exception("Products Cart  count not matching")
    pass

assert(ItemsInCart == 0)  # if receives false fails

# try , catch

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()  # for example when you have pop up

except:
    print("somehow i reach this block")

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()  # for example when you have pop up

except Exception as e:
    print(e)

finally:  # prints whatever happens, cleans
    print("cleaning up resources")  # delete cookies etc.


