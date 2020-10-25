import re
import pyperclip

text = pyperclip.paste()

search = input("Enter pattern to search: ")
replace= input("Enter string to replace with: ")

#reObj = re.compile(search)
try:
    newText = re.sub(search,replace,text)
    pyperclip.copy(newText)
    print("done")
except:
    print("Failed")