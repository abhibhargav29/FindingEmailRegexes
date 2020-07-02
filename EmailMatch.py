import re
import pyperclip

string = pyperclip.paste()

#Finding the email with given domain names
emailRegex = re.compile(r'([a-zA-Z0-9._]+@[a-zA-Z0-9]+)(.com|.co.in|.edu|.gov)')
Found = emailRegex.findall(string)

#concatenation of domain names
i=0
for email in Found:
    Found[i]="".join(email)
    i+=1

#print the results
stringToReturn = "\n".join(Found)
print("The following will be written to clipboard:\n",stringToReturn)

#copy to clipboard
pyperclip.copy(stringToReturn)


