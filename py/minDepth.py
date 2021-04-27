def findDepth(root, count):
	if root == None:
		import sys
		return sys.maxsize

	if root.left == root.right == None:
		return count

	return min(findDepth(root.left, count + 1), findDepth(root.right, count + 1))

def minDepth(root):
	if root == None:
		return 0

	return findDepth(root, 1)