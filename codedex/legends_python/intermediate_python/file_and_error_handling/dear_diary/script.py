

# This opens example file for writing

file = open('diaries.txt', 'w')
file.write("Dear Diary,\n")
file.write("Today was absolutely wild! 🌪️\n")
file.write("I met someone unexpected at the cafe ☕ — we talked for hours.\n")
file.close()

file = open('diaries.txt', 'r')
content = file.read()
print(content)
file.close()


