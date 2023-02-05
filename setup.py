from setuptools import setup

def readme():
    
    with open("README.md") as f:
        README = f.read()
        
    return README


setup(
    
    name = "greeting2023",
    version="1.0.0",
    description = "A basic app for greeting a person",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/MikeTeachesCode/greeting",
    author="Michael S. Russell",
    author_email="miketeachingcode@yahoo.com",
    license="MIT",
    classifiers=[
        
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    
    packages = ["greeting2023"],
    package_dir = {"greeting2023": "greeting2023"},
    include_package_data = False,
    install_requires=["reportlab"]

)
    
    
   