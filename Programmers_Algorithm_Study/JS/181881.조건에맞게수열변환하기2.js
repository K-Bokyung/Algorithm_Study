// https://school.programmers.co.kr/learn/courses/30/lessons/181881

function solution(arr) {
  let answer = 0;
  let x = 0;
  let arr_x = [...arr];

  while (true) {
    let arr_y = arr_x.map((item) =>
      item >= 50 && item % 2 === 0 ? (item /= 2) : item < 50 && item % 2 === 1 ? item * 2 + 1 : item
    );

    if (arr_y.toString() == arr_x.toString()) break;
    arr_x = arr_y;
    x += 1;
  }
  answer = x;

  return answer;
}

const arr = [1, 2, 3, 100, 99, 98];
console.log(solution(arr));
