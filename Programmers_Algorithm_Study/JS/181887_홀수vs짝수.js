// https://school.programmers.co.kr/learn/courses/30/lessons/181887

function solution(num_list) {
  let answer = 0;
  let odd_sum = 0;
  let even_sum = 0;

  num_list.forEach((item, idx) => {
    idx % 2 === 1 ? (odd_sum += item) : (even_sum += item);
  });

  if (odd_sum === even_sum) {
    answer = odd_sum;
  } else {
    odd_sum > even_sum ? (answer = odd_sum) : (answer = even_sum);
  }

  return answer;
}

const num_list = [-1, 2, 5, 6, 3];
console.log(solution(num_list));
