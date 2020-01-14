import md5

counter =  1

pass_in = raw_input("enter the md5 hash here: ")
pwfile = raw_input("enter the passwd file name here: ")

try:
                    pwfile = open(pwfile, "r")
except:
                    print "\nFile not found."
                    quit()

for password in pwfile:
    filemd5 = md5.new(password.strip().hexdigest()
    print "trying passwd nr %d: %s " % (counter, password.strip())

    counter += 1

    if pass_in == filemd5
                      print "\nMatch found. \nPasswd is: %s" % pasword
                      break

else: print "\nPasswd not found."

                
