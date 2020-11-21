# Sudoku-Solver

A school project program that will take an easy sudoku board and solve it

Introduction 

The basic challenge here is to write a Sudoku Solver.  
If you are feeling brave, don't limit it to a 3 by 3 grid. 
To do this well you will need to think very logically. 
Start with only easy problems (that do not need to search). 
Then we want to put a GUI on it. 
Then an interactive GUI 
Then  an sudoku problem maker! 

 

Hints and Tips 

Represent the board as either a 2D array or a 4D array (a 3 x 3 grid of 3 x 3 grids).  

 

Use functions to your advantage – they will be your friend. You will need to structure your code well and you will have multiple loops within loops.  

 

There are 2 reasons why (at this stage) you may put a number in a square: 

1) That is the only place on that column / row / grid that number can go 
2) There is only one number that can go in that square 

 

I would create 2 functions that check these out,  
Then also a function to see if the problem has been solved (and is correct!). 

 

Other functions could be useful include: 

1) Has a particular column / row / grid been solved? 
2) What numbers are in a particular column / row / grid? 
3) What numbers are still needed in a particular column / row / grid? 
4) Does a column / row / grid already have a certain number in it? 

 

You may also want to think a bit efficiently. How could you solve this in a way that you don't have to keep checking the same thing over and over again? Is there any room for recursion? 

 

You may want a method of (in the case where it is insolvable by this method) that the loop stops.  

 

What I want to see 

1) A working program 
2) Some flow charts showing the logic 
3) A brief diary updating me (I'll let you know!) 

 

Suggested tackling order 

1) Have it read a starting sudoku problem from a csv file (I suggest you collaborate on the file structure).  
2) Get it simply to loop through the problem correctly to print it out. One way which will probably help you later is just to create functions to print out complete rows , columns and grids (even if you never use the function). 
3) Write some functions as suggested under hints and tips to help you. 
4) Start putting it all together to solve the problem 
5) Test! 

6) Add GUI – more details to follow 
7) Make it interactive so you can step through the solving process. 
8) Make it go from a sudoku solution to a (new) sudoku problem. 
9) Come up with a sudoku problem from scratch! 
