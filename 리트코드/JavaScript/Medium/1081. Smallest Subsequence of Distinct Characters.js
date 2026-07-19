/**
 * @param {string} s
 * @return {string}
 */
var smallestSubsequence = function(s) {
    console.log('a'.charCodeAt())
    const index = new Array(26).fill(0)

    for (let i = 0; i < s.length; i++){
        index[s.charCodeAt(i) - 97] = i
    }

    const stack = []
    let visited = 0 // 비트용

    console.log(1 << 5)
    for (let i = 0; i < s.length; i++){
        const char = s[i]
        const code = s.charCodeAt(i) - 97
        const mask = 1 << code

        if ((visited & mask) !== 0) {
            continue
        }

        while (
            stack.length > 0 &&
            stack[stack.length - 1] > char &&
            index[stack[stack.length - 1].charCodeAt(0) - 97] > i    
        ) {
            const popChar = stack.pop()
            const popCode = popChar.charCodeAt(0) - 97

            visited &= ~(1 << popCode)
        }

        stack.push(char)
        visited |= mask;
    }

    return stack.join('')
};