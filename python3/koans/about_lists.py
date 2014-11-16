#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    def test_creating_lists(self):
        empty_list = list()
        self.assertEqual(list, type(empty_list))
        #tips      通过len获取长度
        self.assertEqual(0, len(empty_list))

    def test_list_literals(self):
        nums = list()
        self.assertEqual([], nums)

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
        self.assertListEqual([1, 2], nums)
        #tips append  add element
        nums.append(333)
        self.assertListEqual([1, 2, 333], nums)

    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']
        #tips supports negative index start with -1
        #     positive index start from 0
        self.assertEqual('peanut', noms[0])
        self.assertEqual('jelly', noms[3])
        self.assertEqual('jelly', noms[-1])
        self.assertEqual('butter', noms[-3])

    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']
        #tips [start_index, end_index]
        #      start_index default 0
        #      end_index   default length(list)
        #      when out of range return []
        self.assertEqual(['peanut'], noms[0:1])
        self.assertEqual(['peanut', 'butter'], noms[0:2])
        self.assertEqual([], noms[2:2])
        self.assertEqual(['and', 'jelly'], noms[2:20])
        self.assertEqual([], noms[4:0])
        self.assertEqual([], noms[4:100])
        self.assertEqual([], noms[5:0])

    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(['and', 'jelly'], noms[2:])
        self.assertEqual(['peanut', 'butter'], noms[:2])

    def test_lists_and_ranges(self):
        # range(start, end, step)
        #       [start, end)
        #       step default 1, but could be negative num
        self.assertEqual(range, type(range(5)))
        #tips range not equal to list
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
        self.assertEqual([0,1,2,3,4], list(range(5)))
        self.assertEqual([5,6,7,8], list(range(5, 9)))

    def test_ranges_with_steps(self):
        self.assertEqual([0,2,4,6], list(range(0, 8, 2)))
        self.assertEqual([1,4,7], list(range(1, 8, 3)))
        self.assertEqual([5,1,-3], list(range(5, -7, -4)))
        self.assertEqual([5,1,-3, -7], list(range(5, -8, -4)))
        # extend assert
        self.assertEqual([], list(range(5, 8, -4)))

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        # tips insert meaning make inserting element as index element
        knight.insert(2, 'not')
        self.assertEqual(['you', 'shall', 'not', 'pass'], knight)

        knight.insert(0, 'Arthur')
        self.assertEqual(['Arthur','you', 'shall', 'not', 'pass'],
                         knight)

    def test_popping_lists(self):
        # tips element may not be some type
        stack = [10, 20, 30, 40]
        stack.append('last')

        self.assertEqual([10, 20, 30, 40, 'last'], stack)

        popped_value = stack.pop()
        self.assertEqual('last', popped_value)
        self.assertEqual([10,20,30,40], stack)
        # todo
        # tips pop index element
        popped_value = stack.pop(1)
        self.assertEqual(20, popped_value)
        self.assertEqual([10,30,40], stack)

        # Notice that there is a "pop" but no "push" in python?
        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)
        '''
        The Zen of Python, by Tim Peters
        Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to d
        Although that way may not be obvious at first unless you're Dutc
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!
        '''

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last')

        self.assertEqual([1, 2, 'last'], queue)

        popped_value = queue.pop(0)
        self.assertEqual(1, popped_value)
        self.assertEqual([2, 'last'], queue)

        # Note, for Python 2 popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.

        # This is not an issue for Python 3 though

