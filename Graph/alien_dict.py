# Complete the function below.

def find_order(words):
    # if there is only 1 word? r

    # if len(words) == 1:
    #   return words[0]

    # 1) build graph
    #   graph = {a, (indegree, set("b"))}
    # 2) Do topological sort
    graph = build_graph(words)

    # alphabet = ["a","b"]
    alphabet = topological_sort(graph)

    # return string
    return "".join(alphabet)


# return list of vertices in topological order
def topological_sort(graph):
    queue = []
    res = []

    # put all vert with in degree = 0
    for v in graph.keys():
        if graph[v][0] == 0:
            queue.append(v)

    # sort while BFS queue is not empty
    while len(queue) > 0:
        vert = queue.pop(0)
        res.append(vert)

        # update in degree of neighours
        for neighbour in graph[vert][1]:
            in_degree, adj_list = graph[neighbour]
            in_degree -= 1
            graph[neighbour] = in_degree, adj_list

            if in_degree == 0:
                queue.append(neighbour)

    return res


# return graph = {('a', set())}
def build_graph(words):
    graph = {}

    # what if there is only 1 word
    if len(words) == 1:
        for c in words[0]:
            if c not in graph:
                graph[c] = (0, set())

        return graph
    # compare words 1-2, 2-3

    n_words = len(words)
    for i in range(0, n_words - 1):  # till  i = 3
        word1 = words[i]
        word2 = words[i + 1]

        min_len = min(len(word1), len(word2))

        # compare word by characters with min len
        # till

        for j in range(0, min_len):
            c1 = word1[j]
            c2 = word2[j]

            if c1 not in graph:
                graph[c1] = (0, set())

            if c2 not in graph:
                graph[c2] = (0, set())

            # add edge c1 -> c2 to c1 and increase indegree of c2
            if c1 != c2:
                in_degree, adj_list = graph[c1]

                if c2 not in adj_list:
                    adj_list.add(c2)
                    in_degree, adj_list = graph[c2]
                    in_degree += 1
                    graph[c2] = (in_degree, adj_list)
                # break at first diff
                break
            else:
                continue

    return graph


if __name__ == '__main__':
    words = ["baa", "abcd", "abca", "cab", "cad"]
    out = "bdac"

    words = ["a", "b", "ba", "bb", "bc", "dc", "dd"]
    out = "abcd"
    print(find_order(words))
