# https://leetcode.com/problems/most-common-word/description/

import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = [i.lower() for i in banned]
        paragraph = re.sub('[^a-zA-Z0-9]', ' ', paragraph).lower()
        P = [i for i in paragraph.split() if i not in ban]
        answer = collections.Counter(P).most_common()
        
        return answer[0][0]
