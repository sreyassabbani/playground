#include <concepts>
#include <cstddef>
#include <stack>
#include <unordered_set>
#include <vector>

struct Node {
    int value;
    std::vector<Node*> out;
};

struct graph {
    Node& root;
};

template <typename Q, typename T>
concept Container = requires(Q q, T item) {
    { q.empty() } -> std::convertible_to<bool>;
    q.push(item);
    q.pop();
};

template <typename C> auto peek(const C& c) {
    if constexpr (requires { c.top(); }) {
        return c.top();
    } else {
        return c.front();
    }
}

template <template <typename...> typename C>
    requires Container<C<const Node*>, const Node*>
bool cfs(const graph& g, Node& target) {
    C container;
    Node& cur = g.root;
    container.push(cur);

    // theoretically most space this should is g.size;
    // but i'm not sure of a C++ set impl that fixes size.
    std::unordered_set<Node*> read;

    while (!container.empty()) {
        for (Node* n : cur.out) {
            if (!read.contains(n)) container.push(n);
            else read.insert(n);
        }
    }
}

const auto bfs = [](const graph& g, Node& target) -> bool {
    return cfs<std::stack>(g, target);
};
