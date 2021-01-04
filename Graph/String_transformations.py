# Complete the function below.

def string_transformation(words, start, stop):
    # 1) build graph, can be several connected components
    #   vertex - char
    #   edge - transition c1 -> c2
    # 2) iterate start and stop words
    # 3) if chars are different, find path from c1 to c2, form word
    # 4) continue until all transitions are done
    # 5) return resutling list

    # corner cases
    if len(words) == 0 and start != stop:
        return [start, stop]

    if len(words) == 0 and start == stop:
        return ["-1"]

    # graph = {a,(b,c)}
    graph = build_graph(words)

    word_len = len(start)

    transitions = [start]

    t_word = start

    for i in range(0, word_len):
        c1 = start[i]
        c2 = stop[i]

        if c1 == c2:
            continue

        # different
        if not find_path(graph, c1, c2):
            return ["-1"]

        t_word = t_word[:i] + c2 + t_word[i + 1:]
        transitions.append(t_word)

    return transitions


# return graph = {()}
def build_graph(words):
    graph = {}

    words_len = len(words)
    w_len = len(words[0])

    for i in range(0, word_len - 1):
        word1 = words[i]
        word2 = words[i + 1]

        for j in range(0, w_len):
            c1 = word1[j]
            c2 = word2[j]

            if ()

    return graph



if __name__ == '__main__':
