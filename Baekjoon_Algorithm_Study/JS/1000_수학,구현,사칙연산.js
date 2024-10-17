// https://www.acmicpc.net/problem/1000

// 1. 입력값 받기
const nums = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');

const A = parseInt(nums[0]);
const B = parseInt(nums[1]);

// 2. 정답 출력
console.log(A + B);
