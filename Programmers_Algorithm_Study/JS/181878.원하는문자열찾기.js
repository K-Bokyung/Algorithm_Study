// https://school.programmers.co.kr/learn/courses/30/lessons/181878

function solution(myString, pat) {
  let answer = 0;

  myString.toLowerCase().includes(pat.toLowerCase()) ? (answer = 1) : (answer = 0);

  return answer;
}

const myString = 'AbCdEfG';
const pat = 'AbC';
console.log(solution(myString, pat));
