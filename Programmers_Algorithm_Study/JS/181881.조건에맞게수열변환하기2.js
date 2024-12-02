// https://school.programmers.co.kr/learn/courses/30/lessons/181881

function calculation(arr) {
  let arr1 = [];
  for (i = 0; i < arr.length; i++) {
    if (arr >= 50 && arr % 2 === 0) {
      arr1.push(arr[i] / 2);
    } else if (arr < 50 && arr % 2 === 1) {
      arr1.push(arr[i] * 2 + 1);
    } else {
      arr1.push(arr[i]);
    }

    return arr;
  }
}

function solution(arr) {
  let answer = 0;
  let arr1 = [];
  let arr2 = [];
  let x = 1;

  for (i = 0; i <= x; i++) {
    arr1 = calculation(arr);
  }
  console.log(arr1);

  return answer;
}

const arr = [1, 2, 3, 100, 99, 98];
console.log(solution(arr));
