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
include CMakeFiles/remove.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/remove.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/remove.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/remove.dir/flags.make

CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.o: CMakeFiles/remove.dir/flags.make
CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.o: ../数据结构篇/数组/27.移除元素.cpp
CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.o: CMakeFiles/remove.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/baojiali/Projects/leetcode/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.o -MF CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.o.d -o CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.o -c /home/baojiali/Projects/leetcode/数据结构篇/数组/27.移除元素.cpp

CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/baojiali/Projects/leetcode/数据结构篇/数组/27.移除元素.cpp > CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.i

CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/baojiali/Projects/leetcode/数据结构篇/数组/27.移除元素.cpp -o CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.s

# Object files for target remove
remove_OBJECTS = \
"CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.o"

# External object files for target remove
remove_EXTERNAL_OBJECTS =

remove: CMakeFiles/remove.dir/数据结构篇/数组/27.移除元素.cpp.o
remove: CMakeFiles/remove.dir/build.make
remove: CMakeFiles/remove.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/baojiali/Projects/leetcode/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable remove"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/remove.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/remove.dir/build: remove
.PHONY : CMakeFiles/remove.dir/build

CMakeFiles/remove.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/remove.dir/cmake_clean.cmake
.PHONY : CMakeFiles/remove.dir/clean

CMakeFiles/remove.dir/depend:
	cd /home/baojiali/Projects/leetcode/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/baojiali/Projects/leetcode /home/baojiali/Projects/leetcode /home/baojiali/Projects/leetcode/build /home/baojiali/Projects/leetcode/build /home/baojiali/Projects/leetcode/build/CMakeFiles/remove.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/remove.dir/depend

