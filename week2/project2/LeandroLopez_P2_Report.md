# Week 2, Project 2
## CSC6023 - Leandro Lopez

### Experience
Initially, setting up the main() function seemed like it was going to be a breeze. It wasn't difficult setting up a while loop to keep our program, prompting the user for input. Deleting nodes, however, proved more challenging.

After I set up my *num* variable to capture input, I was quickly able to insert nodes or quit the program. Things needed to be smoothed out but there where no major issues. Deleting nodes did give me trouble. I kept getting Attribute errors because I was trying to perform an action on a root who's value was *None.* What I had to do was create a new method that looked for a node, *searchNode.* This method searches a tree and returns False if our element isn't in the tree, True otherwise. That method helped solve our problem because it prevented the *delete_node* method from working on a root with the value *None.*

Once that was all set, I had to go back an replace an *if statement* with a *Try and Except* block just to clean up the code and make sure non-numeric input didn't close out or crash our program.

### Time Complexity  
Our program leverages an AVL tree. Because they are self-balancing, the heights of two child subtrees of any node differ by at most one. This property leads to an O(log n) time complexity. 

Our main function had a while loop that runs until a user quits. The AVL tree operations inside our main function, *search, insert, and delete,* retain the O(log n) time complexity of the AVL tree. Because of this, each iteration of the loop is O(log n) although the overall complexity is determined by the user's input.