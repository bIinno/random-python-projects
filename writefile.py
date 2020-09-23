s = input("Writefile text: \n")
print("Your text has been written to a file named \"writefile.txt\" and should be found in the same directory as this application!")
f = open('writefile.txt', 'w')
f.write(s)
