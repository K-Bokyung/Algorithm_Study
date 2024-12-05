// https://school.programmers.co.kr/learn/courses/30/lessons/181880

function solution(num_list) {
  let answer = 0;
  let turn = 0;
  let list_x = num_list.filter((num) => num > 1);

  while (true) {
    let list_y = list_x.map((item) =>
      item % 2 === 0 ? (item /= 2) : item !== 1 ? (item - 1) / 2 : item
    );

    turn += list_y.length;

    if (list_y.filter((num) => num > 1).length === 0) break;
    list_x = list_y.filter((num) => num > 1);
  }

  answer = turn;

  return answer;
}

const num_list = [12, 4, 15, 1, 14];
console.log(solution(num_list));
