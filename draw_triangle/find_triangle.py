def biggest_triange(nums):
    l = len(nums)

    results = []

    for a in range(0,l):
        for b in range(a+1,l):
            for c in range(b+1,l):
                if nums[a] < nums[b] + nums[c] or nums[b] < nums[a] + nums[c] or nums[c] < nums[b] + nums[a]:
                    n_list = [nums[a], nums[b], nums[c]]
                    n_list.sort()
                    if n_list not in results:
                        results.append(n_list)

    max = [0, 0]

    for i in range(0, len(results)):
        sum = results[i][0] + results[i][1] + results[i][2]
        if sum > max[1]:
            max = [i, sum]

    return results[max[0]], max[1]
