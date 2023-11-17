import sys

from greetings import snake, hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
elif len(sys.argv) == 3:
    snake()

