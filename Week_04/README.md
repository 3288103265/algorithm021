学习笔记
### Week4
## BFS and DFS
1. DFS：深度优先搜索，指优先按照深度对树或者图进行遍历，对于当前节点，首先访问一个子节点，然后继续深入访问子节点的子节点，一直增加树的深度。DFS与前序遍历类似。在实现上，有递归和非递归两种方式，本质上都是使用栈来实现。
	
	a. 递归代码模板
	  ```
	    visited = set()
		def dfs(node, visited):
			if node in visited: # terminator
			# already visited
				return
			visited.add(node)
			# process current node here.
				...
			for next_node in node.children():
				if not next_node in visited: dfs(next_node, visited)
		  		dfs(root.right, visited)

	  ```
	b. DFS栈实现模板：
	  ```
		def dfs(node, visited):
			 if node in visited:
				 return
			 stack = []
			 stack.append(node)

			 while stack:
			   	 node = stack.pop()
				 visited.append(node)

				 process(node)
				 kids = get_kids(node)
				 stack.extend(kids)
	```
	
2. BFS：广度优先搜索，指按照距离当前节点的距离来遍历树或者图，优先遍历当前节点的所有子节点（邻居节点）。一般基于队列来实现，利用队列的先入先出特性，从根节点开始加入到队列。当队列不为空时，队列元素出列，然后将这个节点的所有子节点添加到队列末尾，迭代进行上述过程，完成对树或者图的遍历。应对题型，层序遍历和节点间的最小距离；BFS基于队列实现模板；
	```
	def bfs(node, visied):
		if node in visited:
			return
		queue = deque()
		queue.append(node)
		
		while queue:
			node = queue.popleft()
			visited.append(node)
			
			process(node)
			kids = get_kids(node)
			queue.append(kids)
	```
3. 总结：对于已知节点类型的DFS和BFS，比较容易解决。但是对于节点类型比较抽象，或者需要手动建图的题型，则做起来很吃力，例如，字符串的最下转换序列。
## 贪心算法
1. 贪心和回溯，动态规划的区别：
	a. 贪心法每次寻找到局部最优，不能回退；
	b. 回溯法可以回退；
	c. 动态规划：最优判断+回退
2. 适用条件：子问题的最优解能够获得原问题的最优解。
3. 思路：
	a. 首先要能够证明可以使用贪心算法，即子问题最优能够获得全局最优；
	b. 在不同的角度考虑使用贪心算法，例如从前往后，从后往前，局部切入等；
## 二分查找
1. 适用条件：a）单调有序；b）有上下界；c）使用索引获取数据；
2. 某些情况下，局部有序也可以使用二分查找。
	b. 在不同的角度考虑使用贪心算法，例如从前往后，从后往前，局部切入等；查找
	b. 在不同的角度考虑使用贪心算法，例如从前往后，从后往前，局部切入等；
