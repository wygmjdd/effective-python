

'''
检查工具：
    flake8
    pylint

VS Code配置:
    Python
    Pylance

简单测试几个检测
'''

from inspect import currentframe, getframeinfo

this_is_one_thing = True
that_is_another_thing = True

def do_something():
    cur_frame = currentframe()
    parent_frame = cur_frame.f_back

    parent_frameinfo = getframeinfo(parent_frame)
    cur_frameinfo = getframeinfo(cur_frame)
    print(f'cur lineno is: {cur_frameinfo.lineno}, parent lineno is: {parent_frameinfo.lineno}')  # NOQA
    print(f'cur lineno is: {cur_frameinfo.lineno}, parent lineno is: {parent_frameinfo.lineno} pylinttttttttttttttttttttttttttttttttttt')


# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()


# 一行违背3条规则
import os, sys


# 似乎PEP 8推荐做法也会不被检测
foo = (0,)  # Correct
bar = (0, )  # Wrong
