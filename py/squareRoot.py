def mySqrt(x: int) -> int:
	l, r = 1, x
	sqrt = 0
	while r >= l:
		mid = l + (r - l) // 2
		square = mid ** 2
		if square > x:
			r = mid - 1
		elif square == x:
			return mid
		else:
			l = mid + 1
			sqrt = mid
	return mid if x else 0


if __name__ == '__main__':
	print(mySqrt(int(input())))