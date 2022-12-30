import pathlib

print(pathlib.Path.home())
print(pathlib.Path.cwd())
print(pathlib.Path.home().joinpath("gitworkplace").resolve(True))
read_test_resolve = pathlib.Path.cwd().joinpath("realpython", "test.txt").resolve(True)
with read_test_resolve.open(mode='r') as f:
    print(f.read())
read_test = pathlib.Path.cwd().joinpath("realpython", "test.txt")
with read_test.open(mode='r') as f:
    print(f.read())

print(read_test_resolve.name)
print(read_test_resolve.stem)
print(read_test_resolve.suffix)
print(read_test_resolve.parent)


