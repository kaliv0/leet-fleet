// 118. Pascal's Triangle

function generate(numRows: number): number[][] {
    let triangle = [[1]];
    if (numRows === 1) {
        return triangle;
    }

    for (let i = 1; i < numRows; i++) {
        let innerArr = [1];
        for (let j = 1; j < i; j++) {
            innerArr.push(triangle[i - 1][j - 1] + triangle[i - 1][j]);
        }
        innerArr.push(1);
        triangle.push(innerArr);
    }

    return triangle;
}

console.log(generate(5)); // [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
console.log(generate(1)); // [[1]]
