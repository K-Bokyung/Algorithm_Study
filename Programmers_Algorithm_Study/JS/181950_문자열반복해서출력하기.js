// https://school.programmers.co.kr/learn/courses/30/lessons/181950

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on('line', function (line) {
  input = line.split(' ');
}).on('close', function () {
  str = input[0];
  str_copy = str;
  n = Number(input[1]);
  for (let i = 1; i < n; i++) {
    str += str_copy;
  }
  console.log(str);
});
