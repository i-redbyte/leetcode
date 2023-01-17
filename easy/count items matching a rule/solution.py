from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index = 0
        if ruleKey == "color":
            index = 1
        elif ruleKey == "name":
            index = 2
        result = 0
        for i in items:
            if i[index] == ruleValue:
                result += 1
        return result


print(
    Solution().countMatches(
        items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
        ruleKey="color",
        ruleValue="silver"
    )
)

print(
    Solution().countMatches(
        items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
        ruleKey="type",
        ruleValue="phone")
)
