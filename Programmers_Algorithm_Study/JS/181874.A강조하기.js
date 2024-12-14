// https://school.programmers.co.kr/learn/courses/30/lessons/181874

function solution(myString) {
  let answer = '';
  myString.split('').map((item) => {
    item === 'a'
      ? (answer += item.toUpperCase())
      : item === 'A'
      ? (answer += item)
      : item === ' '
      ? (answer += item)
      : (answer += item.toLowerCase());
  });

  return answer;
}

const myString = 'abstract algebra';
console.log(solution(myString));
