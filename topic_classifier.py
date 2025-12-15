def classify_topic(problem_name):
    name = problem_name.lower()

    rules = {
        "Sliding Window": ["substring", "window"],
        "Array": ["array", "subarray"],
        "HashMap": ["frequency", "count", "duplicate"],
        "Linked List": ["linked", "list", "node"],
        "Stack": ["stack"],
        "Queue": ["queue"],
        "Binary Search": ["binary search"],
        "DP": ["dp", "dynamic"],
        "Graph": ["graph", "dfs", "bfs"],
        "Tree": ["tree", "bst"]
    }

    for topic, keys in rules.items():
        if any(k in name for k in keys):
            return topic

    return "General"
