def pattern_count(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        if text[i : len(pattern) + i] == pattern:
            count += 1
    return count
