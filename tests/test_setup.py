# test_setup.py — check your environment is ready
import sys
import platform
import subprocess

print(f"Python: {sys.version}")
print(f"OS: {platform.system()} {platform.release()}")

# Step 1: Check NVIDIA driver
try:
    result = subprocess.run(["nvidia-smi"], capture_output=True, text=True)
    if result.returncode == 0:
        print("GPU: NVIDIA drivers detected ✓")
    else:
        print("GPU: nvidia-smi failed — NVIDIA driver may not be installed correctly")
except FileNotFoundError:
    print("GPU: nvidia-smi not found — install NVIDIA drivers")
except Exception as e:
    print(f"GPU check failed: {e}")

# Step 2: Check whether PyTorch is installed
try:
    import torch
    print(f"PyTorch: {torch.__version__}")
except ImportError:
    print("PyTorch: not installed")
    print("\n✅ Setup check complete!")
    sys.exit(0)

# Step 3: Check PyTorch GPU / CUDA support
try:
    print(f"PyTorch CUDA build: {torch.version.cuda}")
    print(f"torch.cuda.is_available(): {torch.cuda.is_available()}")

    if torch.cuda.is_available():
        print(f"CUDA device count: {torch.cuda.device_count()}")
        print(f"CUDA device name: {torch.cuda.get_device_name(0)}")
        print("GPU: PyTorch can use the GPU ✓")
    else:
        print("GPU: PyTorch cannot access CUDA")
except Exception as e:
    print(f"PyTorch GPU check failed: {e}")

print("\n✅ Setup check complete!")