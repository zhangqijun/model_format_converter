
from setuptools import setup, find_packages
from os import path
import re

package_name="mfc"
root_dir = path.abspath(path.dirname(__file__))

with open("readme.md") as f:
    long_description = f.read()

with open(path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    print(init_text)
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

setup(
    name=package_name,
    version=version,
    description=\
        "Self-Created Tools to convert deeplearning files from tf,pytorch,onnx,paddle to eachothers. "+
        "The purpose of this tool is to solve the massive Transpose extrapolation problem in deeplearning models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="zqj",
    author_email="zzz9958123@qq.com",
    url="https://github.com/zhangqijun/model_format_converter",
    license="MIT License",
    packages=find_packages(exclude=['test*','json_samples']),
    platforms=["linux", "unix"],
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            "mfc=mfc:main"
        ]
    }
)
