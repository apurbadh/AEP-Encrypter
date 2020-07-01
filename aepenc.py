import random
import string
from os import system as terminal

def encryptFile(filename, passw):
    aList = []
    try :
        file = open(filename)
    except:
        return "Cannot find the file"
    for a in file.readlines():
        aList.append(a)
    wordList = string.ascii_letters + string.punctuation + '1234567890' 
    finalWord = ""
    for i in aList:
        for j in i:
            randomWord = random.choice(wordList)
            aWord = random.choice(wordList)
            bWord = random.choice(wordList)
            finalWord += j + randomWord + aWord + bWord + randomWord 
        finalWord += "\n"

    for a in passw:
        aWord = random.choice(wordList)
        bWord = random.choice(wordList)
        finalWord += a + aWord +bWord + aWord
        
    encFile = open(filename + ".aep", 'w')
    encFile.close()           
    encFile = open(filename + '.aep', 'a')
    encFile.write(finalWord)
    
    file.close()
    encFile.close()           

    return "Done."


def encrypt(word):
    wordList = string.ascii_letters + string.punctuation + '1234567890' 
    finalWord = ""
    
    for i in word:
        randomWord = random.choice(wordList)
        aWord = random.choice(wordList)
        bWord = random.choice(wordList)
        finalWord += i + randomWord + aWord + bWord + randomWord
        
    return finalWord


def passWordCheak(usr, encForm):   
    result = ""
    for i in range(0,len(encForm),4):
        result = result + encForm[i]

    return result == usr
        


def decrypt(encForm):
    result = ""
    for i in range(0, len(encForm), 5):
        result = result + encForm[i]
        
    return result


manual = '''
/////////////////////////////////
|||          (AEP)            |||
|||    encrypt : encryption   |||
|||    help : code manual     |||
|||    decrypt : decryption   |||
|||    -w : words             |||
|||    -f : file              |||
|||    clean : clear screen   |||
|||    close : exit           |||
/////////////////////////////////

'''
decoration = "(aep) >> "
while True:
    choice = input(decoration)
    if choice == "help":
        print(manual)
        
    elif choice == "clean":
        terminal("clear")
        
        
    elif choice[:7] == "encrypt":
        
        if choice[8:10] == '-w':
            words = choice[11:]
            answer = encrypt(words)
            print("\n==> " + answer + "\n")
            
        elif choice[8:10] == '-f':
            fileName = choice[11:].split(" ")[0]
            print("\nCreate a password ")
            passw = input("-> ")
            answer = encryptFile(fileName, passw)
            print(answer)
            
        else:
            print("Command not found!")
    
    
    elif choice[:7] == "decrypt":
        
        if choice[8:10] == '-w':
            theWord = choice[11:]      
            answer = decrypt(theWord)
            print("\n==> " + answer + "\n")
            
        elif choice[8:10] == '-f':
            name = str(choice[11:].split(" ")[0])
            print("Enter the password ")
            passw = input("-> ")
            try:
                file = open(name)
                allLines = []
                for line in file.readlines():
                    allLines.append(line)
                file.close()
                    
                cheak = passWordCheak(passw, allLines[-1])
                if cheak:
                    final = ""
                    for k in range(len(allLines) - 1):
                        answer = decrypt(allLines[k])
                        final = final + answer
                    fileDE = open(name + ".adp", 'w')
                    fileDE.write(final)
                    fileDE.close()
                    fileDE = open(name + ".adp")
                    anotherList = []
                    for l in fileDE.readlines():
                        anotherList.append(l)
                    for g in range(1,len(anotherList)):
                        anotherList[g] = anotherList[g][1:]
                    fileDE = open(name + ".adp", 'w')
                    fileDE.writelines(anotherList)
                    fileDE.close()
                    print("Done.")
                else:
                    print("Incorrect Password.")
            except:
                print("File not found.")
                
        else:
            print("Command not Found.")
            
    elif choice == 'close':
        break
    
    else:
        print("Invalid command")
                    
            

                
                    
            
       
            
            
            
            
        

        
    
        
    
        


