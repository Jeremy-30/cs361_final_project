# Microservice for Bruce
# By: Jeremy Talbert
# CS 361
# February 12th, 2023

import time
import random


def main():
    while True:
        print("Checking for connection...")
        r_int = random.randint(10000, 100000)
        time.sleep(10.0)  # change to speed up/slow down program-
        read_in = open("comm_pipe.txt", "r")
        read_line = read_in.readline()
        read_in.close()

        if read_line == "run":  # can be anything
            write_service = open("num_request.txt", "w")
            print(f"Serving the number: {r_int}")
            write_service.write(f"{r_int}")
            write_service.close()


if __name__ == "__main__":
    main()
