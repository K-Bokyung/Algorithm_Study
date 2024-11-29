// https://school.programmers.co.kr/learn/courses/30/lessons/181886

function solution(names) {
  let answer = [];

  for (i = 0; i < names.length; i += 5) {
    answer.push(names[i]);
  }

  return answer;
}

const names = ['nami', 'ahri', 'jayce', 'garen', 'ivern', 'vex', 'jinx'];
console.log(solution(names));
