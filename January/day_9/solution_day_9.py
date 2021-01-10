def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    length = 1
    visited = set()

    graph = defaultdict(set)
    for word in wordList:
        for i in range(len(word)):
            letter = word[:i] + "_" + word[i + 1:]
            graph[letter].add(word)

    start, finish = {beginWord}, {endWord}
    while start:
        if start & finish:
            return length

        new_start = set()
        for word in start:

            visited.add(word)

            for i in range(len(word)):
                next_words = graph[word[:i] + "_" + word[i + 1:]]
                next_words -= visited
                new_start |= next_words
        length += 1
        start = new_start

        if len(finish) < len(start):
            start, finish = finish, start
    return 0
