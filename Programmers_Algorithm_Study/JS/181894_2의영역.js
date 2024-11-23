// https://school.programmers.co.kr/learn/courses/30/lessons/181894

function solution(arr) {
  let answer = [];

  if (!arr.includes(2)) {
    answer.push(-1);
  } else {
    let idx_list = [];

    arr.forEach((item, idx) => {
      if (item === 2) {
        idx_list.push(idx);
      }
    });

    answer = arr.slice(idx_list[0], idx_list[idx_list.length - 1] + 1);
  }

  return answer;
}

const arr = [1, 2, 1, 2, 1, 10, 2, 1];
console.log(solution(arr));
