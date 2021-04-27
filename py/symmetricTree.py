def isMirror(t1, t2):
	if t1 == t2 == None:
		return True

	if t2 == None or t1 == None:
		return False

	return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)


def symmetric(root):
	return isMirror(root, root)
