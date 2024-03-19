# https://leetcode.com/problems/reorder-data-in-log-files/description/

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter_logs = []
        digit_logs = []
        for i in logs:
            if i.split()[1].isalpha():
                letter_logs.append(i)
            else:
                digit_logs.append(i)
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        answer = letter_logs + digit_logs
        return answer