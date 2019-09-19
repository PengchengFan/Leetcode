# self.n 用数据会内存溢出
class Solution:
    def __init__(self, n_rows: int, n_cols: int):
        self.n = n_rows * n_cols - 1
        self.n_rows, self.n_cols = n_rows, n_cols
        self.removed = []

    def flip(self) -> List[int]:
        index = random.randint(0, self.n)
        while index in self.removed:
            index = random.randint(0, self.n)
        self.removed.append(index)

        return [index // self.n_cols, index % self.n_cols]

    def reset(self) -> None:
        self.removed = []

# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()