def generate_subsequences(s):
    result = []

    def dfs(index, cur):
        if index == len(s):
            result.append(cur)
            return
        dfs(index + 1, cur)
        dfs(index + 1, cur + s[index])

    dfs(0, "")
    return result


s = "abc"
print(generate_subsequences(s))