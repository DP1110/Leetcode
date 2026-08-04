    var sorted = Array(repeating: false, count: 101)
    var mn = 101
    var mx = 0
    for num in nums {
        mn = min(mn, num)
        mx = max(mx, num)
        sorted[num] = true
    }
    var res: [Int] = []
    for i in mn ... mx {
        guard !sorted[i] else { continue }
        res.append(i)
    }

    return res