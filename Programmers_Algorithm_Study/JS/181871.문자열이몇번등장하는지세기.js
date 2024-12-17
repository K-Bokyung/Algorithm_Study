// https://school.programmers.co.kr/learn/courses/30/lessons/181871

function solution(myString, pat) {
  let answer = 0;

  while (myString.length > 0) {
    let str = myString.match(pat);
    answer += 1;
    myString = myString.slice(str.index + 1, myString.length);
    myString.length < pat.length ? (myString = 0) : undefined;
  }

  return answer;
}

const myString = 'aaaa';
const pat = 'aa';
console.log(solution(myString, pat));
