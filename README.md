# Python-Gaming-Project
				Dots and Boxes Game Report
Game rules:
This game is played by 2 people (here user versus computer).Two players start from a rectangular array of dots and take turns to join horizontally or vertically adjacent dots. If a player completes the fourth side of a square (box), he owns the box and must get another chance to play the game.
The player who owns more number of boxes wins the game. 
Aim: to generate algorithm for the computer algorithm to play the game and increase its chances of winning.
Players: user, computer
Terms and variables used:
Dimensions: stores the dimensions of the game board. Example: 2X2, 3X3 etc
BOARDH: array which stores the positions of horizontal edges. Below figure shows the positions of each edge in boardh array.
 

BOARDV: array which stores the positions of vertical edges. Below shows the positions of vertical edges in boardv array.
 
BOX: array which stores the number of edges that occupy the borders of the box.
 	

.
1. Computer’s move:
	When turn shifts to computer, it has following cases.












j





First computer searches for safe boxes available and occupies safe edge if there exist. If there is no safe edge, then computer searches for sacrificial moves available. If there is no possibility for any sacrificial moves, then computer is left to take any edge randomly [random move].

			
								
1.1 Taking safe edges:
	Computer is said to take safe edge when it occupies the edge where the corresponding box has less than 2 sides occupied.
						
                  
			Figure 1.1

As shown in figure 1.1, certain edges can be termed as unsafe for the computer to occupy. Edges at certain positions are said to be unsafe as the corresponding box as 2 or more than 2 sides occupied. 
Condition when the computer occupies the unsafe sides:
Move marked with yellow is made by user. Move marked with red color is made by computer.
 


				        Figure 1.2
If the box with 2 sides is occupied, the corresponding side is said to be unsafe because if the computer occupies the 3rd side, the box is made available for the user and thus the opponent gains a point	.

                                        					
		Figure 1.3							
As shown in figure 1.1, the user faces the following situation. so when user occupies the edge as shown in figure 1.3,the computer gains all 3 sided boxes and occupies the safe edge in box[0][3].
As shown in figure 1.1, the boxes 13 and 23 as unsafe to occupy as they have two sides occupied.
By occupying the safe edges, computer reduces chances for user [opponent] to score points to maximum extent.
Algorithm 1: Safe Sides pseudo code:
	If horizontal edge at i,j is not occupied:
		If box at i,j has no sides or only 1 side occupied:
			Occupy horizontal edge
		Else If box at i-1,j has no sides or only 1 side occupied:
                                          Occupy horizontal edge
		Else if box at imp and i-1, j has no sides or only 1 side occupied:
			Occupy that horizontal edge
		Else:
			Horizontal edge i,j is not a safe edge
     If vertical edge at i,j is not occupied:
		If box at i,j has no sides or only 1 side occupied:
			Occupy horizontal edge
		Else if box at i,j-1 has no sides or only 1 side occupied:
   			Occupy vertical edge
		Else if box at i,j and i,j-1 has no sides or only 1 side occupied:
			Occupy vertical edge 
		Else:
			Vertical edge i,j is not a safe edge
1.2. Sacrificial move:
If there are no safe sides left for the computer to occupy, then it must occupy the side in such a way that the opponent gains less number of boxes and in next turn long chains are available for the computer.
This is one of the situations which computer faces where there are no safe sides. All boxes have at least 2 sides occupied.
                                       
				Figure 2.1
So any move occupied by the computer will lead to opponent (user) to gain one or more boxes.
So computer must place a move in such a way that user gains less number of boxes.
                                 
				Figure 2.2
             
By computer’s move, user will able to gain only one box and thus in user’s next move computer will able to gain more number of boxes than user. So the algorithm is to calculate less unsafe opportunity from a set of unsafe opportunities.
If computer would have placed without analyzing the situation then we get a set of situations to be faced.
Computer can occupy the following vertical and horizontal edges.
Vertical edges :[0,0],[0,1],[0,2].[0,3],[0,4],[1,1],[1,2],[1,3],[2,1],[2,3],[3,2],[3,3]
Horizontal edges:[2,0],[2,2],[2,3],[3,0],[3,1],[3,3],[4,0]
1) Sacrificing 1 box:
          
			Figure 2.3       
 	                                               
         
		Figure 2.4

Computer analyses the number of boxes the opponent will gain by a move and selects the edge which leads to less number of boxes (1 or 2).




Algorithm 2:selection of an edge which gives only one box to the opponent
 If the box has 2 sides occupied:
  If the horizontal side is not occupied:
    If adjacent box having the horizontal side as common side with the box has less than 2 sides:    
         Occupy the horizontal edge
  If the vertical edge is not occupied:
   If adjacent box having this vertical edge as common side with the box has less than 2 sides:
 Occupy the vertical edge

 
Figure 2.5
2) Sacrificing 2 boxes:
     
If there are no chances to lose or sacrifice one box for the opponent or user, then next step the computer takes is to sacrifice minimum number of boxes after 1...ie 2 boxes.
                                               
                                                                         Figure 2.6
As seen above, computer has neither 3 edge nor safe sides to occupy. Computer must occupy the position in such a way that it leaves less number of boxes for the opponent to gain. But in some situations (as shown above), computer cannot sacrifice exactly one box. Thus computer has no other choice other the sacrificing 2 boxes.
So computer occupies the position in such a way that user can occupy 2 boxes.
                                      
					Figure 2.7
 Thus the user gains two boxes and makes a move. This move may open a long chain which makes the computer occupy more number of boxes.

Random move:
    If there are no safe edges or 3 sided edges or no opportunity to sacrifice more than 2 boxes then computer takes a move randomly.
1.3. Scoring the point:
As stated in the game rules, players score when they fill the 4 sides of the box. We can gain box/boxes in two ways.
1. Taking safe boxes and safe edge.
2. Occupying 4th edge of all 3 sided boxes and placing a safe move.
3. Occupying 4th edge of all 3 sided boxes and following the algorithm as shown above when there is no safe edges available.

1.3.1 Taking safe boxes:
	Player who completes the box gains a point.
Now computer faces the following situations as shown in figure 1 and figure 2.
                           
		FIG 3.1.1							FIG 3.1.2
In figure 3.1.1, box [1] [1] has 3 sides occupied. If computer occupies the fourth side, he completes the box and gains a point. Here the computer plays a safe game where there is no scope for the opponent to gain a point.
In figure 3.1.2, if computer occupies the 4th side of box [1] [1], computer gains a point but the 4th side of box [1] [2] is left for the user to occupy and thus opponent completes the box and opponent gains the point. Here computer doesn’t play a safe game.

Algorithm 3:  taking safe boxes
 


						Figure 3.1.2
           
     If a box has 3 sides occupied:
                    If edge2 is not occupied and the adjacent box doesn’t have 2 sides occupied:
                            Occupy the 2nd edge
                    Else if edge 1 is not occupied and adjacent box doesn’t have 2 sides occupied:
		Occupy the 1st edge
                    Else if edge 4 is not occupied and adjacent box doesn’t have 2 sides occupied:
                            Occupy the 4th edge
                    Else if edge 3 is not occupied and adjacent box doesn’t have 2 sides occupied:
		Occupy the 3rd edge
																																	




1.3.2 Filling of boxes and placing a safe move or sacrifice-move or random move:
	If there exits boxes with 3 sides occupied, then the computer must occupy the boxes and place a safe move because when computer gains a point, it gets another chance to play.












 


							Figure 3.2.1

If there doesn’t exist any safe 1 side to occupy then the computer occupies all the boxes and checks any chances for sacrifice or makes any random move.
Algorithm 4: occupying 4th edge of 3 sided box/boxes:
While there are boxes with 3 sides filled:
	Occupy the 4th side and gain a point	
                             n
                      Figure 3.2.1
The computer gains all 3 sided boxes and occupies the safe edge in box [0] [3] according to safe edge algorithm.
