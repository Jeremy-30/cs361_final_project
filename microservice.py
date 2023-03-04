# Microservice for Jeremy
# Bruce Curtis
# CS 361
# February 8th, 2023

import time


def main():
    while True:
        print("Checking for connection...")
        time.sleep(5.0)  # change to speed up/slow down program
        read_in = open("comm_pipe.txt", "r")
        read_line = read_in.readline()
        read_in.close()

        if read_line == "2":
            write_mad2 = open("story.txt", "w")
            print(f"Serving story: 2")
            mad2 = "Pyramids~7~Pyramids are [adjective] tombs where Egyptians [past tense verb] their\n" \
                   "kings and [adjective] families. Some of them are [whole number] years old, each\n" \
                   "taking many [plural noun] to build. Each pyramid had [plural noun] inside and\n" \
                   "were decorated with [plural noun].\n"
            write_mad2.write(mad2)
            write_mad2.close()

        if read_line == "3":
            write_mad3 = open("story.txt", "w")
            print(f"Serving story: 3")
            mad3 = "Art Class~8~Today in Art Class we went outside to draw pictures of trees, flowers and\n" \
                   "[plural noun]. I decided to draw a [adjective] oak tree. First, I drew the trunk\n" \
                   "and then I added the [plural noun]. I colored the trunk [color] and the leaves\n" \
                   "[color]. There was a [noun] in the tree so I drew that too. It had [adjective] red\n" \
                   "feathers. Soon, the teacher came to [verb] my picture.\n"
            write_mad3.write(mad3)
            write_mad3.close()


if __name__ == "__main__":
    main()
