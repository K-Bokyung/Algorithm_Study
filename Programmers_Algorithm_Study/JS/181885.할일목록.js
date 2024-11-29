// https://school.programmers.co.kr/learn/courses/30/lessons/181885

function solution(todo_list, finished) {
  let answer = [];
  let unfinished = [];

  finished.forEach((item, idx) => {
    item !== true ? unfinished.push(idx) : unfinished;
  });

  unfinished.forEach((item) => {
    answer.push(todo_list[item]);
  });

  return answer;
}

const todo_list = ['problemsolving', 'practiceguitar', 'swim', 'studygraph'];
const finished = [true, false, true, false];
console.log(solution(todo_list, finished));
