// https://school.programmers.co.kr/learn/courses/30/lessons/181893

function solution(arr, query) {
  let answer = [];

  query.forEach((item, idx) => {
    if (idx % 2 === 0) {
      arr.splice(item + 1, arr.length);
    } else {
      arr.splice(0, item);
    }
  });

  answer = arr;

  return answer;
}

const arr = [0, 1, 2, 3, 4, 5];
const query = [4, 1, 2];
console.log(solution(arr, query));
