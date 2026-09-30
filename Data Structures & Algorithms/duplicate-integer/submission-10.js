class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let seen = [];
        for (let num of nums){
            if (seen.includes(num) === false){
                seen.push(num);
            }
            else if (seen.includes(num) === true){
                return true;
            }
        }
        return false;
    }
}
