def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup("There were problems", excs)
f()