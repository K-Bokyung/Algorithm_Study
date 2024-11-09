// https://school.programmers.co.kr/learn/courses/30/lessons/181918

function solution(arr) {
  let stk = [];
  let i = 0;

  for (i = 0; i < arr.length; i++) {
    if (stk.length === 0) {
      stk.push(arr[i]);
      continue;
    } else if (stk.length !== 0 && stk[stk.length - 1] < arr[i]) {
      stk.push(arr[i]);
      continue;
    } else if (stk.length !== 0 && stk[stk.length - 1] >= arr[i]) {
      stk.pop();
      i -= 1;
      continue;
    }
  }

  return stk;
}
