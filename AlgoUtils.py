import time


def timer(func):
    def wrapper(*args, **kwargs):
        time1 = time.time()
        ret_value = func(*args, **kwargs)
        time2 = time.time()
        color_print(f"Timer: function {func.__name__} took {(time2 - time1):.2f} seconds", Colors.BLUE)
        return ret_value

    return wrapper


def color_print(msg, color="", end="\n"):
    """
    usage example: color_print("hello world", Colors.BLUE)
    """
    print(color + msg + Colors.END, end=end)


class Colors:
    BLUE = '\033[1;34;48m'
    GREEN = '\033[1;32;48m'
    YELLOW = '\033[1;33;48m'
    RED = '\033[1;31;48m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[1;37;0m'