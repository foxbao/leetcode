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
include CMakeFiles/surrounded_region.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/surrounded_region.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/surrounded_region.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/surrounded_region.dir/flags.make

CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.o: CMakeFiles/surrounded_region.dir/flags.make
CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.o: ../图论/130.被围绕的区域.cpp
CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.o: CMakeFiles/surrounded_region.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/baojiali/Projects/leetcode/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.o -MF CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.o.d -o CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.o -c /home/baojiali/Projects/leetcode/图论/130.被围绕的区域.cpp

CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/baojiali/Projects/leetcode/图论/130.被围绕的区域.cpp > CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.i

CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/baojiali/Projects/leetcode/图论/130.被围绕的区域.cpp -o CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.s

# Object files for target surrounded_region
surrounded_region_OBJECTS = \
"CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.o"

# External object files for target surrounded_region
surrounded_region_EXTERNAL_OBJECTS =

surrounded_region: CMakeFiles/surrounded_region.dir/图论/130.被围绕的区域.cpp.o
surrounded_region: CMakeFiles/surrounded_region.dir/build.make
surrounded_region: CMakeFiles/surrounded_region.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/baojiali/Projects/leetcode/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable surrounded_region"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/surrounded_region.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/surrounded_region.dir/build: surrounded_region
.PHONY : CMakeFiles/surrounded_region.dir/build

CMakeFiles/surrounded_region.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/surrounded_region.dir/cmake_clean.cmake
.PHONY : CMakeFiles/surrounded_region.dir/clean

CMakeFiles/surrounded_region.dir/depend:
	cd /home/baojiali/Projects/leetcode/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/baojiali/Projects/leetcode /home/baojiali/Projects/leetcode /home/baojiali/Projects/leetcode/build /home/baojiali/Projects/leetcode/build /home/baojiali/Projects/leetcode/build/CMakeFiles/surrounded_region.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/surrounded_region.dir/depend

