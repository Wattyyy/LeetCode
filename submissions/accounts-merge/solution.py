from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self, n) -> None:
        self.node_to_depth = {idx: 0 for idx in range(n)}
        self.node_to_par = {idx: idx for idx in range(n)}

    def search_parent(self, x: int) -> int:
        if self.node_to_par[x] == x:
            return x
        else:
            return self.search_parent(self.node_to_par[x])

    def combine(self, x: int, y: int) -> None:
        x, y = self.search_parent(x), self.search_parent(y)
        if x == y:
            return
        x_depth, y_depth = self.node_to_depth[x], self.node_to_depth[y]
        if x_depth <= y_depth:
            self.node_to_par[x] = y
            if x_depth == y_depth:
                self.node_to_depth[y] += 1
        else:
            self.node_to_par[y] = x
        return


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        address_to_ids = defaultdict(list)
        for idx, add_list in enumerate(accounts):
            for _, address in enumerate(add_list):
                if 1 <= _:
                    address_to_ids[address].append(idx)

        uf = UnionFind(n)
        for ids in address_to_ids.values():
            for _ in range(1, len(ids)):
                uf.combine(ids[0], ids[_])

        idx_to_addresses = defaultdict(set)
        for idx, add_list in enumerate(accounts):
            par = uf.search_parent(idx)
            par_add_list = accounts[par]
            for _, address in enumerate(add_list):
                if 1 <= _:
                    idx_to_addresses[par].add(address)
            for _, address in enumerate(par_add_list):
                if 1 <= _:
                    idx_to_addresses[par].add(address)

        ans = []
        for idx, addresses in idx_to_addresses.items():
            tmp = []
            name = accounts[idx][0]
            tmp.append(name)
            tmp.extend(sorted(list(addresses)))
            ans.append(tmp[:])

        return ans

