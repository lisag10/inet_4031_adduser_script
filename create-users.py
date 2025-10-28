#!/usr/bin/python3

# INET4031
# Lisa Guan
# Data Created
# Last Modified:10/27/25


import os #allows running system commands like useradd or passwd
import re #provides tools for working with regular expressions 
import sys #gives access to standard input and command line arguments

def main():
    for line in sys.stdin:

        #This regular expression checks if the line starts with a #
        match = re.match("^#",line)

        #This splits each line from the input file into fields separated by colons
        fields = line.strip().split(':')

        #The IF checks whether the line is a comment or doesn't have enough fields and if either is true, skip the rest of the loop and move to the next line
        if match or len(fields) != 5:
            continue

        #The three lines extract the username, password, and additional information for the user
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #This splits the last field, which contains the user's group
        groups = fields[4].split(',')

        #The print statement shows that a new user account is being created
        print("==> Creating account for %s..." % (username))
        #This builds the Linux command to add a new user with a home directory and gecos info
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #The os.system(cmd) command runs the Linux command stored in 'cmd' to create the new user
        #print cmd
        #os.system(cmd)

        #This print statement shows that user password is being set
        print("==> Setting the password for %s..." % (username))
        #Set the user's password by sending it twice to the passwd command
        #The '-ne' option in echo prints both password entries without adding extra newlines
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #Executes the password setting command
        #print cmd
        #os.system(cmd)

        for group in groups:
            #This IF statement checks that the group name is not blank
            #If the group name is not empty, it adds the user to that group 
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()
