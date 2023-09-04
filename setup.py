from setuptools import setup, find_packages
from pathlib import Path

base_path = Path(__file__).parent
long_description = (base_path / "README.md").read_text()

setup(
    name='claude2', 
    version='1.1.5',  
    author='Nipun',
    license="MIT",
    author_email='nipunbhatia06@gmail.com',
    description='A Python package provides an unofficial api for interacting with the Claude from Anthropic',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Nipun1212/Claude_api',  # Replace with your GitHub repository URL
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=['claude', 'ai', 'claude-ai', 'API', 'requests', 'chatbot'],
    package_dir={
    "": "Claude"
    },
    py_modules=["claude"],
    install_requires=[
        'requests', 'curl_cffi' # List any dependencies your package needs
    ],
    python_requires=">=3.7",
)
