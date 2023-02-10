package p221

type Result struct {
	maxLen int

	nextColIdx     int
	nextInitMaxLen int
}

func getMaxSquareLen(matrix [][]byte, rowSrc int, colSrc int, initMaxLen int) Result {
	rowLen, colLen := len(matrix), len(matrix[0])

	if rowSrc >= rowLen || colSrc >= colLen || matrix[rowSrc][colSrc] == '0' {
		return Result{0, colSrc + 1, 0}
	}

	maxLen := 1
	if maxLen < initMaxLen {
		maxLen = initMaxLen
	}
	for ; rowSrc+maxLen < rowLen && colSrc+maxLen < colLen; maxLen++ {
		for i := 0; i <= maxLen; i++ {
			if matrix[rowSrc+i][colSrc+maxLen] == '0' {
				return Result{maxLen, colSrc + maxLen + 1, 0}
			}
			if matrix[rowSrc+maxLen][colSrc+i] == '0' {
				return Result{maxLen, colSrc + i + 1, maxLen - i - 1}
			}
		}
	}
	return Result{maxLen, colSrc + maxLen, 0}
}

func maximalSquare(matrix [][]byte) int {
	maxLen := 0
	rowLen, colLen := len(matrix), len(matrix[0])
	for rowIdx := 0; rowIdx+maxLen-1 < rowLen; rowIdx++ {
		curMaxLen := 0
		for colIdx := 0; colIdx+maxLen-1 < colLen; {
			rst := getMaxSquareLen(matrix, rowIdx, colIdx, curMaxLen)
			if rst.maxLen > maxLen {
				maxLen = rst.maxLen
			}
			colIdx = rst.nextColIdx
			curMaxLen = rst.nextInitMaxLen
		}
	}
	return maxLen * maxLen
}
