cmake_minimum_required(VERSION 3.2) #最低camke版本需求
PROJECT(leetcode) #创建工程，example为工程名

SET(CMAKE_BUILD_TYPE Debug) #debug模式

add_executable(remove 数据结构篇/数组/27.移除元素.cpp)
add_executable(binary 算法篇/二分查找/704.binary.cpp)
add_executable(max-area-of-island 算法篇/广度优先搜索BFS/695.max-area-of-island.cpp)
add_executable(surrounded_region 图论/130.被围绕的区域.cpp)
add_executable(num-of-island 图论/200.岛屿数量.cpp)
add_executable(num-of-island-BFS 图论/200.岛屿数量_BFS.cpp)
add_executable(max-area-of-island-DFS 图论/695.岛屿的最大面积_DFS.cpp)
add_executable(preorder 数据结构篇/二叉树/遍历/前序遍历/144.二叉树的前序遍历.cpp)
add_executable(isSymmetric 数据结构篇/二叉树/对称/101.对称二叉树.cpp)
add_executable(invertTree 数据结构篇/二叉树/翻转/226.翻转二叉树.cpp)
add_executable(reverseList 数据结构篇/链表/206.反转链表.cpp)
add_executable(removeElements 数据结构篇/链表/203.移除链表元素.cpp)
add_executable(swapPairs 数据结构篇/链表/24.两两交换链表中的节点.cpp)
add_executable(quicksort sort/quicksort.cpp)
add_executable(bubblesort sort/bubbleSort.cpp)
add_executable(maxDepth 数据结构篇/二叉树/求深度/104.二叉树的最大深度.cpp)
add_executable(minDepth 数据结构篇/二叉树/求深度/111.二叉树的最小深度.cpp)
add_executable(lowestCommonAncestor 数据结构篇/二叉树/最近公共祖先/236.二叉树的最近公共祖先.cpp)
add_executable(levelOrder 数据结构篇/二叉树/遍历/层序遍历/102.二叉树的层序遍历.cpp)
add_executable(levelOrder_maxdepth 数据结构篇/二叉树/遍历/层序遍历/104.二叉树的最大深度.cpp)
add_executable(levelOrder_minDepth 数据结构篇/二叉树/遍历/层序遍历/104.二叉树的最小深度.cpp)
add_executable(hasPathSum 数据结构篇/二叉树/路径/112.路径总和.cpp)
add_executable(fib 算法思维/动态规划/509.斐波那契数.cpp)
add_executable(climbStairs 算法思维/动态规划/70.爬楼梯.cpp)
add_executable(minCostClimbingStairs 算法思维/动态规划/746.使用最小花费爬楼梯.cpp)
add_executable(uniquePaths 算法思维/动态规划/62.不同路径.cpp)
add_executable(combine 算法篇/回溯/77.组合.cpp)
add_executable(letterCombinations 算法篇/回溯/17.电话号码的字母组合.cpp)
add_executable(twoSum 数据结构篇/哈希表/1.两数之和.cpp)
add_executable(isAnagram 数据结构篇/哈希表/242.有效的字母异位词.cpp)
add_executable(intersection 数据结构篇/哈希表/349.两个数组的交集.cpp)



