import crypt

def testPass(cryptPass):
    #strip salt from hash
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt',encoding="latin-1")
    count = 1
    #for each word in our test dictionary, encrypt word with salt
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        count = count+1
        if (cryptWord == cryptPass):
            print ("[+] Found Password: " + word + "\n" )
            print('Password found on line ' + str(count))
            return
    print ("[-]" + "Password Not Found.\n")
    print('Total Lines ' + str(count))
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print ("[*] Cracking Password For: " + user)
            testPass(cryptPass)

if __name__=='__main__':
    main()
