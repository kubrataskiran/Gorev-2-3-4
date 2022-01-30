int_max = 4294967296
int_min = -4294967296

class Node: #binary tree nodes
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def isBST(node): #return true if the given tree is a binary search tree
	return (checkBST(node, int_min, int_max))

def checkBST(node, mini, maxi):
	
	if node is None:
		return True #empty tree is BST

	if node.data < mini or node.data > maxi:
		return False # False if this node violates min/max constraint

	return (checkBST(node.left, mini, node.data -1) and #test that the left value is less than the parent node 
		checkBST(node.right, node.data+1, maxi)) #and the right value is greater than the parent node

#test values
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node (7)
root.right.left = Node (5)

if (isBST(root)):
	print ("Yes")
else:
	print ("No")

