cmake_minimum_required(VERSION 3.0)

option(ARM_BUILD "Build for ARM" OFF)

project(SimpleLibrary)

execute_process(COMMAND python3 ${PROJECT_SOURCE_DIR}/script.py)
