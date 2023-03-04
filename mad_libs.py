# CS361 Project
# Mad-Libs @ CLI
# Jeremy Talbert

import time


def intro():
    """Prints the program intro"""
    print('''
 _______________________________________________________________________________________
| Hello! Welcome to 'Mad-Libs @ CLI'. If you would like to jump right in, enter "1".    |
| If you are unfamiliar with what a Mad-Lib is, enter "2". If you are wondering what    |
| a Command-Line Interface is, enter "3". If you would like to exit, enter "4". To      |
| get started, pressing a number on your keyboard and then hitting the "enter" key will |
| allow you to choose an option. P.S. Look for the prompt "Enter: " to enter input.     |
|_______________________________________________________________________________________|     
    ''')


def mad_lib_explain():
    """Prints the program explanation"""
    print('''
Mad-Libs is a template word game where you’ll be asked to enter in words to fill out 
a sentence that will ultimately end in a story of your crafting! Mad-Libs can be 
played as a party game or a pastime and can certainly be a lot of fun! Look for "[]" 
to know what type of word to enter. For example, [noun] or [adjective]. If you’d like 
to play, enter "1". If you want to know what a Command-Line Interface is, enter "3". 
Otherwise, if you would like to exit, enter "4".
    ''')


def cli_explain():
    """Prints command-line explanation"""
    print('''
Command-Line Interfaces are text-based user interfaces used to run programs or interact 
with a computer. In this Command-Line Interface program, you will be asked to enter 
numbers and words. The way to do this is very simple, when I prompt you with an option 
of entering a number, simply hit the number on your keyboard and then hit the enter key! 
You may ask yourself, is it really that simple? Yes! I will do all the heavy lifting and 
all you have to do is make sure to hit enter after each number or word you input! If you 
want to start playing, enter "1". If you'd like to know what a Mad-Lib is, enter "2". 
Otherwise to exit, enter "4". 
    ''')


def ending():
    """Function for program termination"""
    print()
    print("Thank you for using Mad-Libs @ CLI! We hope to see you again soon!")
    exit()


def unrecognized():
    """Function for unrecognized command"""
    print()
    print("Unrecognized command, please try again.")
    print()


def story_select(x):
    """Function for selecting story"""
    print()
    print("Here is your Mad-Lib. Follow the order in which the brackets [] appear to input your words!")
    print()
    print(x.get_body())
    x.user_input()
    print()
    print('Here is your hand crafted Mad-Lib!')
    print()


def next_select():
    """Function for selecting next story"""
    print(
        'If you would like to try the same Mad-Lib again, enter "1". Enter "2" if you want to select\n'
        'another story. To exit, enter "3".')
    print()
    while True:
        next_step = input("Enter: ")
        if next_step == "1":
            print()
            print("Alright, let's try the same Mad-Lib again!")
            break
        elif next_step == "2":
            return True
        elif next_step == "3":
            ending()
        else:
            unrecognized()


def microservice(mad):
    """Function for microservice, takes in a string for a mad-lib number"""
    run_comm = open("comm_pipe.txt", "w")
    run_comm.write(f"{mad}")
    run_comm.close()
    print("Request sent to microservice...")
    time.sleep(10.0)
    print(f"Data received. Mad-Lib {mad} Loaded!")
    contents = ""
    with open("story.txt", "r") as read_mad:
        line = read_mad.readline()
        while line:
            contents += line.strip()
            contents += "\n"
            line = read_mad.readline()
    read_mad.close()
    mad_list = contents.split("~")
    story_name = mad_list[0]
    word_count = mad_list[1]
    body = mad_list[2]

    return MadLibs(story_name, word_count, body)


class MadLibs:
    """Represents a Mad Lib"""

    def __init__(self, title, word_count, body, ):
        self._title = title
        self._body = body
        self._word_count = word_count
        self._user_input = []

    def get_title(self):
        """Get method for title"""
        return self._title

    def get_body(self):
        """Get method for body"""
        return self._body

    def get_word_count(self):
        """Get method for word count"""
        return self._word_count

    def user_input(self):
        """Take user input"""
        x = range(0, int(self._word_count))
        for n in x:
            y = input(f"Enter choice [{n + 1}]: ")
            self._user_input.append(y)
        return self._user_input

    def return_user_input(self):
        """Return user input"""
        return self._user_input


def main():
    # ------------- #
    # Intro Section
    # ------------- #
    intro()
    while True:
        start = input("Enter: ")
        if start == "1":
            break
        elif start == "2":
            mad_lib_explain()
        elif start == "3":
            cli_explain()
        elif start == "4":
            ending()
        else:
            unrecognized()

    # ----------------------------------------------------- #
    # Input new Mad-Libs here following the same format
    # Title
    # Word Count
    # Body
    # Note: 'mad2' and 'mad3' are reserved for microservice
    # ----------------------------------------------------- #
    mad1 = MadLibs(
        "The Magic Computers",
        8,
        "Today, every student has a computer small enough to fit into his [noun]. They can\n"
        "solve any math problem by simply pushing the computer's little [plural noun].\n"
        "Computers can add, multiply, divide, and [present tense verb]. They can also\n"
        "[present tense verb] better than a human. Some computers are [part of body(plural)].\n"
        "Others have a/an [adjective] screen that shows all kinds of [plural noun] and\n"
        "[adjective] figures.\n"
    )

    mad4 = MadLibs(
        "The Comp Sci Student",
        10,
        "Once upon a time, in a(n) [adjective] world, computer science was [verb ending in -ing]\n"
        "every day. Students would [verb] into their classrooms and [adverb] open up their laptops.\n" 
        "They would spend hours [verb ending in -ing] away, writing [adjective] code and debugging\n"
        "their programs. In computer science class, the teacher would [verb] complex algorithms\n"
        "on the board and ask students to [verb] along. The students would [verb] their hands,\n"
        "excited to [verb] their own programs.\n"
    )

    # ----------------- #
    # Program operation
    # ----------------- #
    while True:
        print('''
	Pick a story and we’ll get started crafting a Mad-Lib!
o	1) The Magic Computer
o	2) Pyramids
o	3) Art Class
o	4) The Comp Sci Student
        ''')
        story = input("Enter: ")
        # ------------------------------------------------- #
        # Start of Copy and Paste Execution
        # Change story number and mad number
        # ------------------------------------------------- #
        while True:
            if story == "1":
                # ----------------------------------- #
                # Built-in implementation of mad1
                # ----------------------------------- #
                story_select(mad1)
                arr1 = mad1.return_user_input()
                print(
                    f"Today, every student has a computer small enough to fit into his {arr1[0]}. They can\n"
                    f"solve any math problem by simply pushing the computer's little {arr1[1]}.\n"
                    f"Computers can add, multiply, divide, and {arr1[2]}. They can also\n"
                    f"{arr1[3]} better than a human. Some computers are {arr1[4]}.\n"
                    f"Others have a/an {arr1[5]} screen that shows all kinds of {arr1[6]} and\n"
                    f"{arr1[7]} figures.\n"
                )
                if next_select():
                    break
            if story == "2":
                # ----------------------------------- #
                # Microservice implementation of mad2
                # ----------------------------------- #
                mad2 = microservice(2)
                story_select(mad2)
                arr2 = mad2.return_user_input()
                print(
                    f"Pyramids are {arr2[0]} tombs where Egyptians {arr2[1]} their\n"
                    f"kings and {arr2[2]} families. Some of them are {arr2[3]} years old, each\n"
                    f"taking many {arr2[4]} to build. Each pyramid had {arr2[5]} inside and\n"
                    f"were decorated with {arr2[6]}.\n"
                )
                if next_select():
                    break

            if story == "3":
                # ----------------------------------- #
                # Microservice implementation of mad3
                # ----------------------------------- #
                mad3 = microservice(3)
                story_select(mad3)
                arr3 = mad3.return_user_input()
                print(
                    f"Today in Art Class we went outside to draw pictures of trees, flowers and\n"
                    f"{arr3[0]}. I decided to draw a {arr3[1]} oak tree. First, I drew the trunk\n"
                    f"and then I added the {arr3[2]}. I colored the trunk {arr3[3]} and the leaves\n"
                    f"{arr3[4]}. There was a {arr3[5]} in the tree so I drew that too. It had {arr3[6]} red\n"
                    f"feathers. Soon, the teacher came to {arr3[7]} my picture.\n"
                )
                if next_select():
                    break
            if story == "4":
                # ----------------------------------- #
                # Built-in implementation of mad4
                # ----------------------------------- #
                story_select(mad4)
                arr4 = mad4.return_user_input()
                print(
                    f"Once upon a time, in a(n) {arr4[0]} world, computer science was {arr4[1]}\n"
                    f"every day. Students would {arr4[2]} into their classrooms and {arr4[3]} open up their laptops.\n" 
                    f"They would spend hours {arr4[4]} away, writing {arr4[5]} code and debugging\n"
                    f"their programs. In computer science class, the teacher would {arr4[6]} complex algorithms\n"
                    f"on the board and ask students to {arr4[7]} along. The students would {arr4[8]} their hands,\n"
                    f"excited to {arr4[9]} their own programs.\n"
                )
                if next_select():
                    break


if __name__ == "__main__":
    main()
