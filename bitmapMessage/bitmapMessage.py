"""This program uses a multiline string as a bitmap, a 2D image with only two 
possible colors for each pixel, to determine how it should display a message 
from the user. In this bitmap, space characters represent an empty space, and 
all other characters  are replaced by characters in the user’s message. The 
provided bitmap resembles a world map, but you can change this to any image 
you’d like. The binary simplicity of the space-ormessage-characters system 
makes it good for beginners. Try experimenting with different messages to see 
what the results look like!

The Program in Action
When you run bitmapmessage.py, the output will look like this:

How It Works

Instead of individually typing each character of the world map pattern, you can
copy and paste the whole thing from 
world.txt. A line of 68 periods at the top and bottom of the pattern acts as a 
ruler to help you align it correctly. However, the program will still work if 
you make typos in the pattern. The bitmap.splitlines() method call on line 43 
returns a list of strings, each of which is a line in the multiline bitmap 
string. Using a multiline string makes the bitmap easier to edit into whatever 
pattern you like. The program fills in any non-space character in the pattern, 
which is why asterisks, periods, or any other character do the same thing. The 
message[i % len(message)] code on line 51 causes the repetition of the text in 
message. As i increases from 0 to a number larger than len(message), the 
expression i % len(message) evaluates to 0 again. This causes 
message[i % len(message)] to repeat the characters in message as i increases.
"""

"""Bitmap Message, 
Displays a text message according to the provided bitmap image.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, artistic"""

import sys

# Try changing this multiline string to any image you like:

# There are 68 periods along the top and bottom of this string:
# (You can also copy and paste this string from
# https://inventwithpython.com/bitmapworld.txt)

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print("Bitmap Message, ")
print("Enter the message to display with the bitmap")
message = input("> ")
if message == "":
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == " ":
            # Print an empty space since there's a space in the bitmap:
            print(" ", end="")
        else:
            # Print a character from the message:
            print(message[i % len(message)], end="")
    print() # Print a newline.

"""After enterinf the source code and running it a few times, try making 
experimental changes to it. You can change the string in bitmap to create
entirely new patterns

Exploring the Program

Try to find the answers to the following questions. Experiment with some
modifications to the code and rerun the program to see what effect 
the changes have.

1. What happens if the player enters a blank string for the message?
2. Does it matter what the nonspace characters are in the bitmap variable's
string?
3. What does the i variable created on line 45 represent?
4. What bug happens if you delete or comment out print() on line 52?
"""

