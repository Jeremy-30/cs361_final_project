# Mad-Libs @ CLI
Jeremy Talbert - CS361 Project


# Microservice implementation by Bruce Curtis
My program will request data from the microservice Bruce implemented by writing a request to a 
file called "comm_pipe.txt". My program will write a specific number to comm_pipe.txt that will tell 
the microservice which Mad-Lib it needs to serve my program. 
The Microservice will then write the required information into a text file called "story.txt". My program will then
read the data within story.txt and implement it into a class that it can then use to process new Mad-Lib stories
for users to play with.

# UML Sequence Diagram
![img.png](img.png)