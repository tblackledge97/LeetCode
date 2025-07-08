/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const number = [];

    for (let i=0; i <= arr.length - 1; i++) {
        const x = fn(arr[i], i);
        number.push(x);
    }

    return number;
};