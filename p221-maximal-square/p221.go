package p221

func getMaxSquareLen(matrix [][]byte, rowSrc int, colSrc int, initMaxLen int) int {
	rowLen, colLen := len(matrix), len(matrix[0])

	if rowSrc >= rowLen || colSrc >= colLen || matrix[rowSrc][colSrc] == '0' {
		return 0
	}

	maxLen := 1
	if maxLen < initMaxLen {
		maxLen = initMaxLen
	}
	for ; rowSrc+maxLen < rowLen && colSrc+maxLen < colLen; maxLen++ {
		for i := 0; i <= maxLen; i++ {
			if matrix[rowSrc+i][colSrc+maxLen] == '0' {
				return maxLen
			}
			if matrix[rowSrc+maxLen][colSrc+i] == '0' {
				return maxLen
			}
		}
	}
	return maxLen
}

func maximalSquare(matrix [][]byte) int {
	maxLen := 0
	rowLen, colLen := len(matrix), len(matrix[0])
	for rowIdx := 0; rowIdx+maxLen-1 < rowLen; rowIdx++ {
		curMaxLen := 0
		for colIdx := 0; colIdx+maxLen-1 < colLen; colIdx++ {
			curMaxLen = getMaxSquareLen(matrix, rowIdx, colIdx, curMaxLen)
			if curMaxLen > maxLen {
				maxLen = curMaxLen
			}
			curMaxLen--
		}
	}
	return maxLen * maxLen
}
