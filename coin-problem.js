const generateCoins = (amount) => {
    if (amount === 24) {
        return [5, 5, 7, 7]
    } else if (amount === 25) {
        return [5, 5, 5, 5, 5]
    } else if (amount === 26) {
        return [5, 7, 5, 7, 7]
    } else if (amount === 27) {
        return [7, 7, 5, 5]
    } else if (amount === 28) {
        return [7, 7, 7, 7]
    }

    const coins = generateCoins(amount - 5)
    coins.push(5)
    return coins
}

const findMax = (n) => {
    const arr = generateCoins(n)
    console.log(n)
    if (arr.length === 0) {
        return n
    } else {
        return findMax(n + 1)
    }
}

console.log(findMax(24))
