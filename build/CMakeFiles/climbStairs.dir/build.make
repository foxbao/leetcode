# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/baojiali/Projects/leetcode

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/baojiali/Projects/leetcode/build

# Include any dependencies generated for this target.
include CMakeFiles/climbStairs.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/climbStairs.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/climbStairs.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/climbStairs.dir/flags.make

CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.o: CMakeFiles/climbStairs.dir/flags.make
CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.o: ../算法思维/动态规划/70.爬楼梯.cpp
CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.o: CMakeFiles/climbStairs.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/baojiali/Projects/leetcode/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.o -MF CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.o.d -o CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.o -c /home/baojiali/Projects/leetcode/算法思维/动态规划/70.爬楼梯.cpp

CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/baojiali/Projects/leetcode/算法思维/动态规划/70.爬楼梯.cpp > CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.i

CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/baojiali/Projects/leetcode/算法思维/动态规划/70.爬楼梯.cpp -o CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.s

# Object files for target climbStairs
climbStairs_OBJECTS = \
"CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.o"

# External object files for target climbStairs
climbStairs_EXTERNAL_OBJECTS =

climbStairs: CMakeFiles/climbStairs.dir/算法思维/动态规划/70.爬楼梯.cpp.o
climbStairs: CMakeFiles/climbStairs.dir/build.make
climbStairs: CMakeFiles/climbStairs.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/baojiali/Projects/leetcode/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable climbStairs"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/climbStairs.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/climbStairs.dir/build: climbStairs
.PHONY : CMakeFiles/climbStairs.dir/build

CMakeFiles/climbStairs.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/climbStairs.dir/cmake_clean.cmake
.PHONY : CMakeFiles/climbStairs.dir/clean

CMakeFiles/climbStairs.dir/depend:
	cd /home/baojiali/Projects/leetcode/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/baojiali/Projects/leetcode /home/baojiali/Projects/leetcode /home/baojiali/Projects/leetcode/build /home/baojiali/Projects/leetcode/build /home/baojiali/Projects/leetcode/build/CMakeFiles/climbStairs.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/climbStairs.dir/depend

