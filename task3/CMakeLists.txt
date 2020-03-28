cmake_minimum_required(VERSION 3.0)

option(ARM_BUILD "Build for ARM" OFF)

if(ARM_BUILD)
    set(CMAKE_CXX_COMPILER "${TOOLCHAIN}/arm-linux-gnueabihf-g++")
    set(CMAKE_C_COMPILER "${TOOLCHAIN}/arm-linux-gnueabihf-gcc")
endif()

project(SimpleLibrary)

execute_process(COMMAND python3 ${PROJECT_SOURCE_DIR}/script.py ${PROJECT_SOURCE_DIR}/filefile)
file(READ ${PROJECT_SOURCE_DIR}/filefile content)
message(INFO ${content})
