cmake_minimum_required(VERSION 3.2) #最低camke版本需求
PROJECT(leetcode) #创建工程，example为工程名

SET(CMAKE_BUILD_TYPE Debug) #debug模式

add_executable(remove 数据结构篇/数组/27.移除元素.cpp)

