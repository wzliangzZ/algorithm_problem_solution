# 左偏树即维护一定的顺序，又保证树的深度在logn级别。
# 通过比较v[x]来定顺序，通过dist[x]来控制树的深度。
"""

左偏树 是一种具有 左偏 性质的 堆有序 的二叉树。
左偏树存储信息：左右结点lc[x],rc[x]、权重v[x]和距离dist[x]。

外结点：左儿子或右儿子为空的结点
结点距离：该结点到最近的外结点经过的边数。
规定：外结点距离为0，空结点距离为-1

性质1：(小根堆) 任意结点v[x]<=v[lc[x]],v[rc[x]]
性质2：(左偏性) 左儿子距离 >= 右儿子距离，dist[lc] >= dist[rc]
性质3：任意结点距离 = 右儿子距离 + 1，dist[x] = dist[rc] + 1
性质4：(保证了时间复杂度为logn) 一颗 n 个结点的二叉树，dist[根] <= log(n+1)-1

合并操作 是左偏树最重要的操作：
1.维护堆性质，先取较小的根作为合并后的根，再 递归合并 其 右儿子 与另个一堆，作为合并后的堆的右儿子。
2.维护左偏性质，合并后若左儿子的dist小于右儿子，则交换。

"""

N = 10 ** 5
v = [0] * N
lc, rc = [0] * N, [0] * N
dist = [0] * N

def merge(x: int, y: int) -> int:
    # 若一个堆为空，则返回另一个堆
    if x == 0 or y == 0: return x + y
    # 取小根堆(让x为小根堆)，若v值一样则比较结点编号
    if x > y if v[x] == v[y] else v[x] > v[y]: x, y = y, x
    #递归合并右儿子和另一个堆
    rc[x] = merge(rc[x], y)

    #维护左偏性质
    if dist[lc[x]] < dist[rc[x]]: lc[x], rc[x] = rc[x], lc[x]
    # 更新距离
    dist[x] = dist[rc[x]] + 1
    return x