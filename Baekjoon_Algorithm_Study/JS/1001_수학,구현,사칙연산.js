// https://www.acmicpc.net/problem/1001

// 1. 입력값 받기
const fs = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');

const A = fs[0];
const B = fs[1];

// 2. 결과값 출력
console.log(A - B);
