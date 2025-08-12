from setuptools import setup, find_packages

setup(
    name="task-cli",
    version="0.0.1",
    packages=find_packages(),
    py_modules=["task_cli", "consts"],
    entry_points={
        "console_scripts": [
            "task-cli=task_cli:main",
        ],
    },
)