const katex = require('katex');

function removeNestedBraces(line) {
    // 用于存储所有替换记录的数组
    const replacementLogs = [];
    
    // 递归处理函数
    function processNode(currentNode) {
        // 如果是数组，递归处理每个元素
        if (Array.isArray(currentNode)) {
            return currentNode.map(item => processNode(item));
        }
        
        // 如果不是对象，直接返回
        if (typeof currentNode !== 'object' || currentNode === null) {
            return currentNode;
        }
        
        // 先处理body中的所有子节点
        if (currentNode.body) {
            currentNode.body = processNode(currentNode.body);
            
            // 检查是否需要替换当前节点
            if (currentNode.type === 'ordgroup' && 
                Array.isArray(currentNode.body) && 
                currentNode.body.length === 1 && 
                currentNode.body[0] && 
                currentNode.body[0].type === 'ordgroup') {
                
                // 记录替换信息（只在有loc值时记录）
                if (currentNode.loc && currentNode.body[0].loc) {
                    replacementLogs.push({
                        replacedSpan: [currentNode.loc.start, currentNode.loc.end],    // 被取代节点的loc
                        replacingSpan: [currentNode.body[0].loc.start, currentNode.body[0].loc.end]  // 取代节点的loc
                    });
                }
                
                // 用子节点替换当前节点，并继续处理替换后的节点
                return processNode(currentNode.body[0]);
            }
        }
        
        // 处理其他可能包含子节点的属性
        for (const key in currentNode) {
            if (key !== 'body' && typeof currentNode[key] === 'object' && currentNode[key] !== null) {
                currentNode[key] = processNode(currentNode[key]);
            }
        }
        
        return currentNode;
    }
    
    // 处理根节点
    const tree = katex.__parse(line, {strict: 'ignore'})
    const modifiedTree = processNode(tree);
    
    const mask = new Array(line.length).fill(true)
    // 返回处理后的树和替换记录
    for (const log of replacementLogs){
        if (log.replacedSpan[0] <= log.replacingSpan[0] && log.replacedSpan[1] >= log.replacingSpan[1]){
            for (let i = log.replacedSpan[0]; i < log.replacingSpan[0]; i++){
                mask[i] = false
            }
            for (let i = log.replacingSpan[1]; i < log.replacedSpan[1]; i++){
                mask[i] = false
            }
        }
    }
    const charArray = line.split('')
    const filteredArray = charArray.filter((_, index) => mask[index])
    const filtered = filteredArray.join('')
    return {
        filtered,
        modifiedTree
    }
}

// const line = '{ \\vdots }'
// const line = '\\left ( \\begin{array} { l l l } { \\rho _ { 1 1 } } & { \\cdots } & { \\rho _ { 1 d } } \\\\ { \\vdots } & { \\ddots } & { \\vdots } \\\\ { \\rho _ { d 1 } } & { \\cdots } & { \\rho _ { d d } } \\end{array} \\right ) \\Longrightarrow \\left ( \\begin{array} { l } { \\rho _ { 1 1 } } \\\\ { \\rho _ { 1 2 } } \\\\ { \\vdots } \\\\ { \\rho _ { 1 d } } \\\\ { \\vdots } \\\\ { \\rho _ { d d } } \\end{array} \\right ) .'
const line ='\\begin{array} { l } { \\rho _ { 1 1 } } \\\\ { \\vdots } \\\\ { \\rho _ { d d } } \\end{array}'

const {filtered, modifiedTree} = removeNestedBraces(line)
console.log(filtered)
console.log(modifiedTree[0].body[0])