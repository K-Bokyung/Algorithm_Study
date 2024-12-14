// https://school.programmers.co.kr/learn/courses/30/lessons/181873

function solution(my_string, alp) {
  let answer = '';
  my_string.includes(alp)
    ? my_string.split('').map((item) => {
        item === alp ? (answer += item.toUpperCase()) : (answer += item);
      })
    : (answer = my_string);

  return answer;
}

const my_string = 'programmers';
const alp = 'p';
console.log(solution(my_string, alp));
