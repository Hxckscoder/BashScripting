**Script to copy a file multiple times**
This is a bash script that prompts the user to enter the name of the file they want to copy and the number of times they want to copy it. Then, it uses a loop to copy the file as many times as specified by the user.

**Requirements**

- This script should be run on CentOS8 or any Linux system with bash shell.
- The user running the script should have read and write permissions on the file to be copied and on the directory where the copied files will be stored.

**How to use**

1. Open a terminal and navigate to the directory where the script is saved.
2. Make the script executable using the command: # chmod +x copy_file.sh.
3. Run the script using the command: ./copy_file.sh.
4. Enter the name of the file you want to copy and the number of times you want to copy it, separated by a space.
5. Press Enter and the script will start copying the file.
The copied files will be stored in the same directory as the original file, with a numerical suffix added to the file name. For example, if the original file name is file.txt and you choose to copy it 3 times, the copied files will be named file1.txt, file2.txt, and file3.txt.