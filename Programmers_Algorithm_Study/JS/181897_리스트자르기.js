// https://school.programmers.co.kr/learn/courses/30/lessons/181897

function solution(n, slicer, num_list) {
  let answer = [];
  let a = slicer[0];
  let b = slicer[1];
  let c = slicer[2];

  if (n === 1) {
    answer = num_list.slice(0, b + 1);
  } else if (n === 2) {
    answer = num_list.slice(a, num_list.length);
  } else if (n === 3) {
    answer = num_list.slice(a, b + 1);
  } else if (n === 4) {
    let new_list = num_list.slice(a, b + 1);

    new_list.forEach((item, index) => {
      c % 2 === 0 && index % 2 === 0 ? answer.push(item) : undefined;
      c === 3 && index % c !== 1 ? answer.push(item) : undefined;
    });

    c === 1 ? answer.push(0) : undefined;
  }

  return answer;
}

const n = 4;
const slicer = [1, 5, 1];
const num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9];

console.log(solution(n, slicer, num_list));
