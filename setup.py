from setuptools import setup, find_packages
import os

setup(
    name="wavtokenizer",
    version="0.1.0",
    description="WavTokenizer: A discrete audio tokenizer for speech, music, and audio processing",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    author="Jisheng Peng and WavTokenizer Contributors",
    author_email="your.email@example.com",  # Replace with your email or leave as is
    url="https://github.com/your-username/WavTokenizer",  # Update to your forked repo URL
    packages=find_packages(),  # Automatically find packages in encoder/, decoder/, etc.
    include_package_data=True,  # Include non-code files like configs/*.yaml
    package_data={
        "wavtokenizer": ["configs/*.yaml"],  # Include configuration files
    },
    install_requires=[
        "torch",
        "torchaudio",
        "hydra-core",
        "scipy",
        "einops",
        "pyyaml",
        "huggingface_hub",
        "encodec",
        "matplotlib",
        "transformers",
        "pytorch-lightning",
        "tensorboardX",
        "soundfile",
        "numpy",
        "jsonargparse[signatures]",
        "torchcrepe",
        "librosa",
        "pesq",
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",  # Adjust if repo uses a different license
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "wavtokenizer-infer=wavtokenizer.infer:main",  # Optional: Add if infer.py has a main() function
        ],
    },
)
