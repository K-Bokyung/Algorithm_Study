// https://www.acmicpc.net/problem/10869

// 1.입력값 받기
const fs = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');

const A = parseInt(fs[0]);
const B = parseInt(fs[1]);

// 2.정답 출력
console.log(A + B);
console.log(A - B);
console.log(A * B);
console.log(Math.floor(A / B));
console.log(A % B);
