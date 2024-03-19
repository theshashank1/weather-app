from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("weather.html")  # Render weather.html from templates folder


if __name__ == "__main__":
    app.run(debug=True)















# from typing import List
#
#
# def insert( intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#     n = len(intervals)
#     i = 0
#     res = []
#
#     # Case 1: No overlapping before merging intervals
#     while i < n and intervals[i][1] < newInterval[0]:
#         res.append(intervals[i])
#         i += 1
#
#     # Case 2: Overlapping and merging intervals
#     while i < n and newInterval[1] >= intervals[i][0]:
#         newInterval[0] = min(newInterval[0], intervals[i][0])
#         newInterval[1] = max(newInterval[1], intervals[i][1])
#         i += 1
#     res.append(newInterval)
#
#     # Case 3: No overlapping after merging newInterval
#     while i < n:
#         res.append(intervals[i])
#         i += 1
#
#     return res


print(insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))


# class Solution :
#     def findMaxLength(self, nums: List[int]) -> int :
#         hashmap = {0 : -1}
#         ans = 0
#         prefixSum = 0
#         for i, num in enumerate(nums) :
#             prefixSum += 1 if num == 1 else -1
#             if prefixSum not in hashmap :
#                 hashmap[prefixSum] = i
#             else :
#                 ans = max(ans, i - hashmap[prefixSum])
#         return ans
#
#
# if __name__ == '__main__' :
#     s = Solution()
#     print(s.findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]))
