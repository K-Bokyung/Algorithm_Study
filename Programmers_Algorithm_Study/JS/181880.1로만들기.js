// https://school.programmers.co.kr/learn/courses/30/lessons/181880

function solution(num_list) {
  let answer = 0;
  let x = 0;
  let idx = 0;
  let list_x = [...num_list];

  while (true) {
    let num = num_list[idx];
    let num2 = num % 2 === 0 ? (num /= 2) : num !== 1 ? (num - 1) / 2 : num;
    console.log('num_list', num2);

    if (num !== 1) {
      num = num2;
      console.log('if문 실행');
    } else {
      idx += 1;
    }
    x += 1;

    if (num === 1 && idx === num_list.length - 1) break;
  }

  answer = x;

  return answer;
}

const num_list = [12, 4, 15, 1, 14];
console.log(solution(num_list));
