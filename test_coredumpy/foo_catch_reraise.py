import sys
import traceback


class ErrorWrapper:
    def __init__(self, exc_info=None, where="in foo()"):
        if exc_info is None:
            exc_info = sys.exc_info()
        self.exc_type = exc_info[0]
        self.exc_msg = "".join(traceback.format_exception(*exc_info))
        tb = traceback.extract_tb(exc_info[2])[-1]  # 获取最后一帧的堆栈信息
        self.where = f"in {tb.filename}, line {tb.lineno}, function {tb.name}"


    def reraise(self):
        msg = f"Caught {self.exc_type.__name__} {self.where}.\nOriginal traceback:\n{self.exc_msg}"
        raise IndexError(msg) from None

def foo(arr):
    for i in range(10):
        print(arr[i])

if __name__ == "__main__":
    l = list(range(9))

    try:
        foo(l)
    except IndexError:
        # 捕获IndexError并封装后重新抛出
        wrapper = ErrorWrapper()
        wrapper.reraise()