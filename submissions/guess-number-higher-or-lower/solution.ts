/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	            -1 if num is lower than the guess number
 *			             1 if num is higher than the guess number
 *                       otherwise return 0
 * var guess = function(num) {}
 */


function guessNumber(n: number): number {
    let left = 1;
    let right = n;
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        let res = guess(mid);
        if (res === 0) {
            return mid;
        }
        else if (res === 1) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
};
