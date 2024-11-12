// https://school.programmers.co.kr/learn/courses/30/lessons/181916

function solution(a, b, c, d) {
  let answer = 0;
  let num_list = [a, b, c, d].sort();
  let num_set = new Set(num_list);

  // 1. 모두 같은 숫자
  if (num_set.size === 1) {
    answer = 1111 * a;
  }
  // 2. 모두 다른 숫자
  else if (num_set.size === 4) {
    answer = num_list[0];
  }
  // 3. 두 개씩 같은 값
  else if (num_set.size === 2 && num_list[1] !== num_list[2]) {
    let p = num_list[0];
    let q = num_list[2];
    (p + q) * (p - q) < 0 ? (answer = -((p + q) * (p - q))) : (answer = (p + q) * (p - q));
  }
  // 4. 두 개만 같은 값
  else if (num_set.size === 3) {
    let p = num_list[0];
    let q = num_list[2];
    let r = num_list[3];
    q === num_list[1] ? ((p = num_list[1]), (q = num_list[0])) : undefined;
    r === num_list[2] ? ((p = num_list[2]), (q = num_list[0]), (r = num_list[1])) : undefined;
    answer = q * r;
  }
  // 5. 세 개만 같은 값
  else if (num_set.size === 2 && num_list[0] !== num_list[3]) {
    let p = 0;
    let q = 0;
    num_list.lastIndexOf(num_list[0]) !== 0
      ? ((p = num_list[0]), (q = num_list[3]))
      : ((p = num_list[3]), (q = num_list[0]));
    answer = (10 * p + q) ** 2;
  }

  return answer;
}
