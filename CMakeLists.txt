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

