#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def happy():
    print("Happy birthday to you!")


def sing(person):
    happy()
    happy()
    print("Happy birthday, dear", person + "!")
    happy()


def main():
    sing("Mike")
    print()
    sing("Lily")
    print()
    sing("Elmer")


main()
