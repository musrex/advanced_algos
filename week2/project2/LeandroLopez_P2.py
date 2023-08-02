from LeandroLopez_AVL import *

def main():
    ''' Main function 
    This is our main function. It instantiates the AVLTree class and the root node.
    It runs on a while loop, prompting the user for input. Their input gets added to 
    the AVL tree, deletes a node from the tree, or closes the program.

    The program only accepts numeric inputs. If input is non-numeric, it will ignore the
    value and return an error. 

    Negative values will stop the while loop, ending the program.

    If the input is unique, it will be added to the tree. If the value already exists,
    it will be deleted from the tree.

    Input: Integers
    Output: Prints an AVL tree in post order
    '''
    tree = AVLTree()
    root = None

    run = True

    while run:
        try:
            num = int(input('''Enter Number. 
Enter a non-positive integer to exit.
Enter the number again to delete it.
=====================================
'''))
            if num <= 0:     
                run = False
                break
            else:
                if root is None: # insertion
                    root = tree.insert_node(root, num)
                elif tree.searchNode(root, num): # deletion
                    root = tree.delete_node(root, num)
                else: # insertion
                    root = tree.insert_node(root, num)

                print(f'Project 2 AVL Tree')
                tree.printHelper(root, '', True)
        except:
            print('Error. Please try again.')
    


if __name__ == "__main__":
    main()