// https://school.programmers.co.kr/learn/courses/30/lessons/181949

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on('line', function (line) {
  input = [line];
}).on('close', function () {
  str = input[0];
  result = '';
  for (i = 0; i < str.length; i++) {
    let sample = str[i].toUpperCase();
    if (str[i] === sample) {
      result += str[i].toLowerCase();
    } else {
      result += str[i].toUpperCase();
    }
  }
  console.log(result);
});
