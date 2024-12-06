// https://school.programmers.co.kr/learn/courses/30/lessons/181878

function solution(myString, pat) {
  let answer = 0;
  let low_string = myString.toLowerCase();
  let low_pat = pat.toLowerCase();
  let first_s = low_pat[0];

  if (myString.length < pat.length && !low_string.split('').includes(first_s)) {
    return answer;
  }

  console.log('if문 넘어옴');

  return answer;
}

const myString = 'aaAA';
const pat = 'aa';
console.log(solution(myString, pat));
