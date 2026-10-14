"""Task 1: verify that the required libraries are installed."""
import importlib
import sys

packages = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn", "torch", "tensorflow"]

print("Python:", sys.version.split()[0])
for name in packages:
    try:
        module = importlib.import_module(name)
        print(f"[OK]      {name:<12} {getattr(module, '__version__', 'unknown version')}")
    except ImportError:
        print(f"[MISSING] {name:<12} install it as described in task_01_installation.md")
