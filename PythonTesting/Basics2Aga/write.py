#first method
file = open("text.txt")
file.close()
# Second method in just one line
# read the file and store all the lines in list
# reverse the list
# write back to the text file
with open ('text.txt', 'r') as reader:  # it opens and closes the file  # 'r' read mode
    content = reader.readlines()  # [abc, bvdsf, cat, dog]
    reversed(content)  # [elephant. dog, cat. bvdsf, abc]
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)





