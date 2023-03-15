# Battle_of_Warships_py
this repository includes my fourth assignment which is given at coursed named Introduction to Programming 1 
the assignment's mission is to write a code of Battle of Warships game
you can learn how to run the code and all other information that you are curious about code, by reading Report.pdf 
but if you don't have time to read the report and want to run the code without wasting time, here are a few information that will help you :
1- the game is played on a grid of ten to ten. Columns of grid are represented by letters, rows by numbers.

2- "Player1.in" and "Player2.in" files include moves that players played. You should check out these files to understand main concept of moves. 
    Thus you can write your own movement.
    
3- it's time to place your ships. First of all, you have a total of 9 ships. There are 5 types of ships in the game (B,C,D,S,P)
   (the length of each type of ship is different from the other). There are 2 from ship B, 4 from ship P and one from the other three ships. 
   You have to place your all ships on the grade.      
   
4- So how do you place your ships? "OptionalPlayer1.txt", "OptionalPlayer2.txt","Player1.txt" and "Player2.txt" are files that you be able to place your warships across
   the map.
   you should check out the Player1.txt and Player2.txt files to understand the main concept of placing ships. 
   then place your ships on wherever you want. 
   next to the right and next to the left of each semicolon (as well as the semicolons at the ends of the lines) are the parts where you will place your ships
   the final step of the ship placement is as follows: we need you to rewrite the coordinates where you placed the ships of type B and P in a different concept. 
   you will easily understand this concept if you check the OptionalPlayer1.txt and OptionalPlayer2.txt files. 
   when writing different concepts of locations to "OptionalPlayer1.txt" and "OptionalPlayer2.txt" files, make sure that they are the same as their locations in the "Player1.txt" and "Player2.txt" files.
5- Now we can run our code : 
   -  create an empty output file called Battleship.out
   -  then put these total 5 files that you prepared python file named "Assignment4.py" in a folder. 
   -  then open your terminal and copy the path to the folder containing all the files and 
      move the terminal to that folder with the cd command
   - then type the newt statement in the terminal ( you must enter the file names correctly in the parts in quotes or the program will not work!)
      : python3 Assignment4.py "Player1.txt" "Player2.txt" "Player1.in" "Player2.in"
   - then you can open the "Battleship.out" file and see who won pr whether the match ended in a draw. There are articles
     seperated by round numbers in this output file. By scrolling up the file, you can see which of yours moves has produced results.
   
