
function selectionSort(nums) {
    for (let i = 0; i < nums.length - 1; i++) {
        let maxI = i;

        for (let j = i + 1; j < nums.length; j++) {
            if (nums[j] > nums[maxI]) {
                maxI = j;
            }
        }

        [nums[i], nums[maxI]] = [nums[maxI], nums[i]];
    }

    return nums;
}

let grades = [4, 2, 5, 3, 5, 4, 3];

console.log("По убыванию:", selectionSort([...grades]));
