from LeandroLopez_AVL import *

def main():
    ''' Main function 
    This function instantiates out AVLTree class and inserts nodes into the tree

    Input: None
    Output: Prints the tree in post order
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