text = input("> Get text: ")
length = len(text)
count = 0
pali = True
while length is not count:
    if (text[count].lower == text[length-1].lower):
        continue
    else:
        print("Not Palindrom!")
        pali = False
        break
if pali:
    print("Palindrom")
