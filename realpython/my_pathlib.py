import pathlib

# /home/eric
print(f"home: {pathlib.Path.home()}")
# /home/eric/gitworkplace/python_notes/realpython
print(f"cwd: {pathlib.Path.cwd()}")

home_path = pathlib.Path.home()
gitworkplace_path = home_path.joinpath("gitworkplace")
print(f"gitworkplace path: {gitworkplace_path}")  # /home/eric/gitworkplace/python_notes/realpython

# non exist path
non_exist_path = home_path.joinpath("non_exist_path")
print(f"non_exist_path: {non_exist_path}")  # /home/eric/non_exist_path

# reading and writing files
read_path = pathlib.Path.cwd().joinpath('read_test.md')
# we can do traditionally
with open(read_path, mode='w') as fid:
    pass
# or we can do
with read_path.open(mode='w') as fid:
    pass

# resolve
print("#### resolve path ####")
resolve_path = pathlib.Path("test.md")
print(f"before resolve: {resolve_path}")
print(f"after resolve: {resolve_path.resolve()}")
resolve_not_exist_path = pathlib.Path("not_exist")
print(f"none_exist after resolve: {resolve_not_exist_path.resolve()}")

# path components
component_path = resolve_path.resolve()
print(f"path.name: {component_path.name}")
print(f"file name without suffix: {component_path.stem}")
print(f"suffix: {component_path.suffix}")
print(f"path.parent: {component_path.parent}")
print(f"path.parent.parent: {component_path.parent.parent}")

# recursive dir
print(f"recursive list: {list(component_path.parent.parent.rglob('*'))}")