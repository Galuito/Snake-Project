# Welcome to the Snake Project!
In this repository you'll find all of my python modules related to learning how to use pygame and me discovering useful and ingenious integrations of methods, you'll notice that some files even have 'marks' which means that they have and upgraded version or simply that I found another way to integrate them into a module.\
The final objective of this module is developing a snake game that has the basic features of one, such features are:
* Picking up the arrow keys for movement
* Managing the snake and its body
* Being able to eat fruit
* All the game over possibilities (screen border or biting itself)\
It's important to remember that this project is for me to learn how to develop a game, I'm not looking for a direct tutorial in how to make the snake game, from the knowledge I have which comes from Coding Train mostly and from the questions that I'm making to chatGPT I am finding the pieces that will allow me to make the Snake Game.

# Nathaniel's Notes
While developing this program, I've noticed that there are a lot of ways to solve the same problem, ones which I thought were inefficient and actually were and some others that I praised but turned out to be really inefficient.\
I noticed that when you're working inside of a while True loop that has the responsibility of keeping your code working is better to not do another loop inside which limits the checks that are supposed to be done outside of said inner loop, therefore, it's better to work with ifs and check if an elapsed time has passed so that you can continue working, this also means that for loops that have a relation with time may have to be avoided because of how they function, in summary, there are many workarounds that a programmer can do in order to solve these problems and not everything has to do the same, it all depends on the situation that you find yourself in and what are your needs.\
TL:DR Don't do loops inside your game loop, do checks using ifs and don't rely on **pygame.time.delay()**