// https://school.programmers.co.kr/learn/courses/30/lessons/181871

function solution(myString, pat) {
  let answer = 0;

  if (myString.includes(pat)) {
    for (i = 0; i < myString.length; i++) {
      let str_s = myString.slice(i, myString.length);
      str_s.includes(pat)
        ? ((myString = str_s), (answer += 1), (i = myString.match(pat).index))
        : (myString = '');
    }
  }

  return answer;
}

const myString = 'aaaa';
const pat = 'aa';
console.log(solution(myString, pat));
