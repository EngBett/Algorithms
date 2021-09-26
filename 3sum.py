def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = {"indices": [], "result": []}

    for i in range(len(nums)):
        t = 0 - nums[i]
        d = {}
        for j in range(len(nums)):
            if i != j:
                x = t - nums[j]
                if x in d:
                    indices = [i, j, d[x]]
                    indices.sort()
                    result = [nums[indices[0]], nums[indices[1]], nums[indices[2]]]
                    result.sort()
                    if indices not in res["indices"] and result not in res["result"]:
                        res["indices"].append(indices)
                        res["result"].append(result)
                        break

                else:
                    d[nums[j]] = j

    print(res)
    return res["result"]


print(three_sum([-1, 0, 1, 2, -1, -4]))
