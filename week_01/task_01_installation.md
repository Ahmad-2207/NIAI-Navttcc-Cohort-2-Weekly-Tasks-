# Task 1: Installation (Week 1)

Install Anaconda3, PyTorch, TensorFlow 2.0, VSCode and PyCharm.
Software installs happen on your own machine, so this file gives the exact steps
and a verification script (`task_01_verify_install.py`) to prove everything works.

## 1. Anaconda3
1. Download the installer for your OS from https://www.anaconda.com/download
2. Windows: run the .exe, choose "Just Me", keep defaults.
   Linux: `bash Anaconda3-<version>-Linux-x86_64.sh`
3. Open a new terminal (Anaconda Prompt on Windows) and check: `conda --version`

## 2. Create an environment for the course
```
conda create -n navttc-ai python=3.10 -y
conda activate navttc-ai
conda install numpy pandas matplotlib seaborn scikit-learn jupyter -y
```

## 3. PyTorch (CPU build is enough for the course)
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```
(For an NVIDIA GPU, pick the matching command at https://pytorch.org/get-started/locally/)

## 4. TensorFlow 2.x
```
pip install tensorflow
```

## 5. VSCode
Download from https://code.visualstudio.com/ then install the "Python" and "Jupyter" extensions.
Select the interpreter with Ctrl+Shift+P, "Python: Select Interpreter", choose `navttc-ai`.

## 6. PyCharm
Download the free Community Edition from https://www.jetbrains.com/pycharm/download/
In Settings, Project, Python Interpreter, add the existing conda environment `navttc-ai`.

## 7. Verify
Run: `python task_01_verify_install.py`
