// https://school.programmers.co.kr/learn/courses/30/lessons/181872

function solution(myString, pat) {
  let answer = '';
  let last_index = myString.lastIndexOf(pat);
  answer = myString.slice(0, last_index + pat.length);

  return answer;
}

const my_string = 'AAAAaaaa';
const pat = 'a';
console.log(solution(my_string, pat));
