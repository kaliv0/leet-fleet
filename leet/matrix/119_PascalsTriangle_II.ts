// 119. Pascal's Triangle II

function getRow(rowIndex: number): number[] {
    let currRow = [1];
    for (let i = 1; i <= rowIndex; i++) {
        let nextRow = [1]
        for (let j = 1; j < i; j++) {
            nextRow.push(currRow[j - 1] + currRow[j]);
        }
        nextRow.push(1);
        currRow = nextRow;
    }
    return currRow;
}

console.log(getRow(3)); // [1,3,3,1]
console.log(getRow(0)); // [1]
console.log(getRow(1)); // [1,1]
