// https://school.programmers.co.kr/learn/courses/30/lessons/181871

function solution(myString, pat) {
  let answer = 0;
  let first_pat = myString.indexOf(pat);
  answer += 1;
  myString.slice(first_pat + 1, myString.length) > 0
    ? (myString = myString.slice(first_pat + pat.length, myString.length))
    : undefined;

  console.log(myString.slice(first_pat + 1, myString.length));

  // while (myString.length > 0) {
  //   let str = myString.slice(first_pat + 1, myString.length);
  //   str.search(pat) ? (str = s) : (myString = '');
  // }

  return answer;
}

const myString = 'banana';
const pat = 'ana';
console.log(solution(myString, pat));
