// https://school.programmers.co.kr/learn/courses/30/lessons/181916

function solution(a, b, c, d) {
  let answer = 0;
  let num_list = [a, b, c, d].sort();
  let num_set = new Set(num_list);

  if (num_set.size === 1) {
    answer = 1111 * a;
  } else if (num_set.size === 2 && num_list[1] === num_list[2]) {
    let p = 0;
    let q = 0;
    num_list.lastIndexOf(num_list[0]) === 0 ? (p = a) : (q = a);
    q !== a ? (q = b) : (p = a);
    answer = (10 * p + q) ** 2;
  } else if (num_set.size === 2 && num_list[1] !== num_list[2]) {
    let p = num_list[0];
    let q = num_list[2];
    let num = (p + q) * (p - q);
    num < 0 ? (answer = -num) : (answer = num);
  } else if (num_set.size === 3) {
    let p = num_list[0];
    let q = num_list[2];
    let r = num_list[3];
    q === num_list[1] ? ((p = num_list[1]), (q = num_list[0])) : (q = num_list[2]);
    r === num_list[2]
      ? ((p = num_list[2]), (q = num_list[0]), (r = num_list[3]))
      : (r = num_list[3]);
    answer = q * r;
  } else if (num_set.size === 4) {
    answer = num_list[0];
  }

  return answer;
}

const a = 2;
const b = 5;
const c = 2;
const d = 6;
console.log(solution(a, b, c, d));
