# INET4031 Add Users Script and User List
## Program Description
Detailed and helpful description paragraph goes here. Describe how the program will help the user. It should talk about how the program is an automated way for the user to accomplish the manual task of adding users. Also include a description of what commands a user would normally use to add a user and then describe how those SAME COMMANDS are used by the script and automated.

This program is designed to automate the manual process of adding new users to a Linux system. Usually, a system administrator would need to run multiple commands manually for each user. This program eliminates the repetitive work, by reading user information from an input file and executing the same commands automatically. The adduser command creates accounts, sets passwords, and assigns users to groups. This saves time and makes user management more efficient.
## Program User Operation
The program reads a list of user account details from an input file and processes each line automatically. For every line read it extracts the username, password, first name, last name, and group. Then it executes system commands to create user account, set password, and assign the user to a group. Additionally, if the line is missing many fields, it is skipped. The user can perform a dry-run to test and see what commands would be executed before making changes to the system.

This section should start off with a paragraph description, then have subsections for the following:
### Input File Format
Each line in the input file represents a user account and must follow this format:
username:password:last_name:first_name:groups
If a user should not be added to a group, use "-" in the group field.
### Command Excuction
To run the script you have to make it executable by using:
chmod a+x create-users.py
Then you can run the program using:
./create-users.py < create-users.input
### "Dry Run"
If a user selects a dry-run they would have to comment out the os.system(cmd) lines and look at the printed commands in the terminal. This shows what would happen without modifying the system. A dry-run is helpful for testing the input file and program are correct before making real changes. 
