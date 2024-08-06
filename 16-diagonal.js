const getMatrix = (matrix, matrixLength, diagonalCount) => {
    if (matrix.length === matrixLength) {
        const diagonals = matrix.flat(1).filter(item => item !== 0).length
        if (diagonals === diagonalCount) {
            console.log(matrix)
        }
        return
    }
    const permute = (perm) => {
        if (perm.length === matrixLength) {
            if (matrix.length === 0 && getIsLinearValid(perm)) {
                matrix.push(perm)
                getMatrix(matrix, matrixLength, diagonalCount)
                matrix.pop()
            } else if (getIsLinearValid(perm) && getIsExtendable(matrix[matrix.length - 1], perm)) {
                matrix.push(perm)
                getMatrix(matrix, matrixLength, diagonalCount)
                matrix.pop()
            }
            return
        }

        const items = [-1, 0, 1];

        items.forEach(item => {
            perm.push(item);
            permute(perm, matrixLength);
            perm.pop();
        });
    };

    permute([])
}

const getIsExtendable = (top, bottom) => {


    for (const [index, value] of bottom.entries()) {


        if (value === 1) {
            if (top[index + 1] === 1 || top[index] === -1) {
                return false
            }
        }

        if (value === -1) {
            if (top[index - 1] === -1 || top[index] === 1) {
                return false
            }
        }
    }

    return true
}

const getIsLinearValid = (arr) => {
    for (const [index, value] of arr.entries()) {
        if (value === 1 && arr[index + 1] === -1 || value === -1 && arr[index + 1] === 1) {
            return false
        }
    }

    return true
}

getMatrix([], 5, 16)



