function countB(s){
    var count = 0
    for (let i = 0; i < s.length; i++) {
        if (s[i] === "B") {
            count++;
        }
    }
    return count;
}

function countChar(s, letter) {
    var count = 0
    for (let i = 0; i < s.length; i++) {
        if (s[i] === letter) {
            count++;
        }
    }
    return count;
}

console.log(countB("BigBigBig"))
console.log(countChar("hello","l"))
