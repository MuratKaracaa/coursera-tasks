const generatePermutations = (perm, n) => {
    let result = [];

    if (perm.length === n) {
        result.push([...perm]);
        return result;
    }

    for (let i = 0; i < n; i++) {
        if (!perm.includes(i)) {
            perm.push(i);
            if (getIsExtendable(perm)) {
                result = result.concat(generatePermutations(perm, n));
            }
            perm.pop();
        }
    }

    return result;
};

const getIsExtendable = (perm) => {
    const latestIndex = perm.length - 1;
    for (let i = 0; i < latestIndex; i++) {
        if (latestIndex - i === Math.abs(perm[latestIndex] - perm[i])) {
            console.log(perm)
            return false;
        }
    }
    return true;
};

const permutations = generatePermutations([], 8);

