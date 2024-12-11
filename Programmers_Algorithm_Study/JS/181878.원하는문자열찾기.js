// https://school.programmers.co.kr/learn/courses/30/lessons/181878

function solution(myString, pat) {
  let answer = 0;
  let low_string = myString.toLowerCase().split('');
  let low_pat = pat.toLowerCase().split('');

  if (myString.length < pat.length && !low_string.includes(low_pat[0])) {
    answer = 0;
  }

  if (
    low_string.slice(low_string.indexOf(low_pat[0]), low_pat.length).join('') === low_pat.join('')
  ) {
    answer = 1;
  }

  return answer;
}

const myString = 'AbCdEfG';
const pat = 'aBc';
console.log(solution(myString, pat));
