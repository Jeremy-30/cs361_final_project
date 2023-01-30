# CS361 Project
# Mad-Libs @ CLI
# A command-line version of the story crafting game/puzzle known as Mad-Libs

class MadLibs:
    """    Represents a Mad Lib    """
    def __init__(self, title, mad_topic, body):
        self._title = title
        self._mad_topic = mad_topic
        self._body = body

    def get_title(self):
        """        Get method for title        """
        return self._title

    def get_topic(self):
        """        Get method for topic        """
        return self._mad_topic

    def body(self):
        """        Get method for body        """
        return self._body


# def main():
#     while True:
while True:
    print('''
     _____________________________________________________________________________________________________________
    | Hello! Welcome to Mad-Libs @ CLI. If you’re unfamiliar with what a Mad-Libs is, enter 1 for a introduction. |
    |     If you are familiar and want to jump right in, enter 2. If you’ve had your fun, enter 3 to exit.        |
    |_____________________________________________________________________________________________________________|
      P.S. If you don’t know what a Command-Line Interface is, your in luck because I’m about to explain it! 
      Command-Line Interfaces are text-based user interfaces used to run programs or interact with a computer. 
      In this Command-Line Interface program, you will be asked to enter numbers and words. The way to do this is 
      very simple, when I prompt you with an option of entering a number, simply hit the number on your keyboard 
      and then hit the enter key! You may ask yourself, is it really that simple? Yes! I will do all the heavy 
      lifting and all you have to do is make sure to hit enter after each number or word you input!
    ''')
    start = input("Enter: ")

    if start == "1":
        print('''
      Mad-Libs is a template word game where you’ll be asked to enter in words to fill out a sentence that will 
      ultimately end in a story of your crafting! Mad-Libs can be played as a party game or a pastime and can 
      certainly be a lot of fun! If you’d like to play, enter 1, otherwise enter 2 and we can go our separate ways!
        ''')
        intro = input("Enter: ")
        if intro == "1":
            start = "2"
        elif intro == "2":
            start = "3"
        else:
            start = "4"

    if start == "2":
        print('''
      	Pick a topic and we’ll get started crafting a Mad-Libs!
      o	1) History
      o	2) Science 
      o	3) Art
      o	4) etc...
        ''')
        topic = input("Enter: ")
        if topic == "1":
            print("This is where I will use the mad-libs class and logic to allow the user to enter their responses"
                  "and be able to backtrace if they want to change their responses")
        if topic == "2":
            print("2")
        if topic == "3":
            print("3")
        if topic == "4":
            print("4")
        if topic == "5":
            print("5")

    # End condition
    if start == "3":
        print('''
    Thanks for playing, we hope to see you again soon!
        ''')
        break

    # Error checking
    if start == "4":
        print("Unrecognized command, please try again")
