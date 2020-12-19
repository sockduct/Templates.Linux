#
# James Small
# SDEV-###-##, <Season> Semester <Year>
# Week # Assignment
# Date:  x #, 2020
# Problem #
# Version:  12-13-2020-01
#
# <Program Name> Makefile
#
# Helpful References:
# * Managing Projects with GNU Make, 3rd Edition:
#   https://learning.oreilly.com/library/view/managing-projects-with/0596006101/
# * For a true cross-platform solution, consider CMake:
#   https://cmake.org/
#

#
# Variables:
#
# C Compiler:
CC := gcc  # Could also use clang
# C Standard:
CSTD := -std=c17
# C++ Compiler:
CXXC := g++  # Could also use clang++
# C++ Standard:
CXXSTD := -std=c++17
# C Compiler Flags:
CFLAGS := -pedantic -pedantic-errors -Wall -Wextra -Werror
# C++ Compiler Flags:
CXXFLAGS := -pedantic -pedantic-errors -Wall -Wextra -Werror
# C Compiler Flags, Relaxed (allow warnings):
RELAXCFLAGS := -pedantic -Wall -Wextra
# C Compiler, Debug Flags:
DFLAGS := -ggdb3
# Linker Flags:
LDFLAGS := -lm -pthread
# Optimize Flags:
OFLAGS := -O3
# Sanitizer Flags:
SFLAGS := -fsanitize=address
SHELL := dash  # dash because no ANSI/Color escape codes in output


#
# Targets:
#
# Notes:
# *  $@ matches the target name, "week#proj" in this case
# *  $^ matches the list of all prerequisites, "week#proj.c" in this case
# *  The "#" is intended to be replaced by the current week number,
#    e.g., s/week#proj/week8proj/g
week#proj: week#proj.c  # Default (must be first target)
	$(CC) $(CFLAGS) $(DFLAGS) -o $@ $^

all:
	week#proj record

clean:
	rm -f week#proj week#proj.o week#proj-run.tmp week#proj-run.txt

help:
	@printf "Make Targets:\n"
	@printf "all        -  build main programs/targets\n"
	@printf "clean      -  remove all created files\n"
	@printf "example    -  build this week's lab/example program\n"
	@printf "help       -  this option\n"
	@printf "record     -  run program and record output\n"
	@printf "week#proj  -  build this week's assigned program (default)\n\n"

# Note:  May or may not want -x option depending on if tabs are desired
record: week#proj
	# Setup datafile so always start from same place:
	# @printf "Setting up starting datafile.\n"
	# cp datafile.start datafile
	@printf "Launching separate shell to minimize extra control characters.\n"
	@printf "record.sh is used to start the program and capture its exit status:\n"
	$(SHELL) -c "script -c \"./record.sh $<\" $(<)-run.tmp"
	@printf "Stripping extra control characters from 'script' output file:\n"
	col -x < $(<)-run.tmp > $(<)-run.txt
	@printf "Cleaning up temporary script file:\n"
	rm -f $(<)-run.tmp

example: example.c  # Example code for the week
	$(CC) $(CFLAGS) $(DFLAGS) -o $@ $^
