from setuptools import setup, find_packages

with open("README.md") as f:
  long_description = f.read()

setup(
  name="random_algorithm",
  version="1.1.0",
  description="A random number generator based on shuffled English words, their ASCII values, and the current epoch time to create highly randomized outputs",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/EDM115/random-algorithm",
  author="EDM115",
  license="MIT",
  classifiers=[
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Topic :: Software Development",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3"
  ],
  project_urls={
    "Documentation": "https://github.com/EDM115/random-algorithm",
    "Funding": "https://github.com/EDM115#support-me-",
    "Source": "https://github.com/EDM115/random-algorithm",
    "Tracker": "https://github.com/EDM115/random-algorithm/issues",
  },
  packages=find_packages(),
  include_package_data=True,
    package_data={
      "random_algorithm": ["wordlist.txt"],
    },
)
