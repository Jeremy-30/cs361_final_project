def intro():
    print('''
     _____________________________________________________________________________________________________________
    | Hello! Welcome to 'Mad-Libs @ CLI'. If you would like to jump right in, enter "1". If you are unfamiliar    |
    | with what a Mad-Lib is, enter "2". If you are wondering what a Command-Line Interface is, enter "3". If     |
    | you would like to exit, enter "4". To get started, pressing a number on your keyboard and then hitting the  |
    | "enter" key will allow you to choose an option. P.S. Look for the prompt "Enter: " to enter input :)        |
    |_____________________________________________________________________________________________________________|     
    ''')


def mad_lib_explain():
    print('''
    Mad-Libs is a template word game where you’ll be asked to enter in words to fill out a sentence that will 
    ultimately end in a story of your crafting! Mad-Libs can be played as a party game or a pastime and can certainly
    be a lot of fun! Look for "**" to know what type of word to enter. For example, **noun** or **adjective**. 
    If you’d like to play, enter "1". If you want to know what a Command-Line Interface is, enter "3". Otherwise, 
    if you would like to exit, enter "4".
    ''')


def cli_explain():
    print('''
    Command-Line Interfaces are text-based user interfaces used to run programs or interact with a computer.
    In this Command-Line Interface program, you will be asked to enter numbers and words. The way to do this is
    very simple, when I prompt you with an option of entering a number, simply hit the number on your keyboard
    and then hit the enter key! You may ask yourself, is it really that simple? Yes! I will do all the heavy
    lifting and all you have to do is make sure to hit enter after each number or word you input! If you want to 
    start playing, enter "1". If you'd like to know what a Mad-Lib is, enter "2". Otherwise to exit, enter "4". 
    ''')


def ending():
    print()
    print("Thank you for using Mad-Libs @ CLI! We hope to see you again soon!")
    exit()


def unrecognized():
    print()
    print("Unrecognized command, please try again.")
    print()


def story_select(x):
    print(x.get_body())
    x.user_input()
    print()
    print('Here is your hand crafted Mad-Lib!')
    print()


def next_select():
    print(
        'If you would like to try again, enter "1". Enter "2" if you want to select another story. '
        'To exit, enter "3".')
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


class MadLibs:
    """    Represents a Mad Lib    """
    def __init__(self, title, word_count, body, ):
        self._title = title
        self._body = body
        self._word_count = word_count
        self._user_input = []

    def get_title(self):
        """        Get method for title        """
        return self._title

    def get_body(self):
        """        Get method for body        """
        return self._body

    def get_word_count(self):
        """        Get method for word count        """
        return self._word_count

    def user_input(self):
        """        take user input        """
        x = range(0, self._word_count)
        for n in x:
            y = input(f"Enter choice {n + 1}: ")
            self._user_input.append(y)
        return self._user_input

    def return_user_input(self):
        """        return user input        """
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

    # ------------------------------------------------- #
    # Input new Mad-Libs here following the same format
    # Title
    # Word Count
    # Body
    # ------------------------------------------------- #
    mad1 = MadLibs \
        ("The Magic Computers",
         8,
         '''
    Today, every student has a computer small enough to fit into his **noun**. They can solve any math problem by simply
    pushing the computer's little **plural noun**. Computers can add, multiply, divide, and **present tense verb**. 
    They can also **present tense verb** better than a human. Some computers are **part of body (plural)**. Others have 
    a/an **adjective** screen that shows all kinds of **plural noun** and **adjective** figures.
    '''
         )

    # ----------------- #
    # Program operation
    # ----------------- #
    while True:
        print('''
    	Pick a story and we’ll get started crafting a Mad-Lib!
    o	1) The Magic Computers
    o	2) History
    o	3) Art
        ''')
        story = input("Enter: ")
        # ------------------------------------------------- #
        # Start of Copy and Paste Execution
        # Be sure to change to the correct story number and
        # 'mad' to the correct mad[number]!
        # ------------------------------------------------- #
        while True:
            if story == "1":
                story_select(mad1)
                arr1 = mad1.return_user_input()
                print(
                    f"Today, every student has a computer small enough to fit into his {arr1[0]}. They can solve\n"
                    f"any math problem by simply pushing the computer's little {arr1[1]}. Computers can add,\n"
                    f"multiply, divide, and {arr1[2]}. They can also {arr1[3]} better than a human. Some computers\n"
                    f"are {arr1[4]}. Others have a/an {arr1[5]} screen that shows all kinds of {arr1[6]} and\n"
                    f"{arr1[7]} figures.\n"
                )
                if next_select():
                    break


if __name__ == "__main__":
    main()
