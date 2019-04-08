import os

pid = os.fork()
if pid < 0:
    print("Fail to Run fork()")
elif pid == 0:
    print("This is SubProcess(%s), FatherProcess is (%s)" %(os.getpid(),os.getppid()) )
else:
    print("This is SubProcess(%s), FatherProcess is (%s)" %(os.getpid(),os.getppid()) )

print("print")