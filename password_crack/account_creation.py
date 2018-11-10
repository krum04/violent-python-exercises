import crypt

def fileWriter(username,password):
    passFile = open("passwords.txt",'w')
    hashPass = crypt.crypt(password,'NX')
    passFile.write(username + ' : ' + hashPass)
    passFile.close()

def main():
    username = input('Please Enter New User:     ')
    password = input('Please Enter New Password: ')
    fileWriter(username,password)

if __name__ == "__main__":
    main()
