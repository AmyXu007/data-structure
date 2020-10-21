# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        
        # src_parent = self.get_parent(src)
        # dst_parent = self.get_parent(dst)
        src_root = self.get_parent(src)
        dst_root = self.get_parent(dst)
        if src_root == dst_root:
            return

        if self.ranks[src_root] >= self.ranks[dst_root]:
            self.parents[src_root] = dst_root
        else:
            self.parents[dst_root] = src_root
            if self.ranks[src_root] == self.ranks[dst_root]:
                self.ranks[src_root] += 1

        self.row_counts[dst_root] += self.row_counts[src_root]
        self.row_counts[src_root] = 0

        if self.max_row_count < self.row_counts[dst_root]:
            self.max_row_count = self.row_counts[dst_root]
        # if src_parent == dst_parent:
        #     return False

        # # merge two components
        # # use union by rank heuristic
        # # update max_row_count with the new maximum table size
        # return True

    def get_parent(self, table):
        # find parent and compress path
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
