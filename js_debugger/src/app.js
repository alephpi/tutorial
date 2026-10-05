// 简单的示例函数，用于演示调试
function add(a, b) {
    // 在这里设置断点或添加 debugger 语句
    // debugger;
    return a + b;
}

function multiply(a, b) {
    let result = 0;
    // 循环中设置断点可以观察每次迭代
    for (let i = 0; i < b; i++) {
        result = add(result, a);
    }
    return result;
}

// 主程序
const num1 = 5;
const num2 = 3;

const sum = add(num1, num2);
const product = multiply(num1, num2);

console.log(` sum: ${num1} + ${num2} = ${sum}`);
console.log(`product: ${num1} × ${num2} = ${product}`);
