from setuptools import setup, find_packages

setup(
    name="vizblend",
    version="3.0.0",
    author="Mahmoud Housam",
    author_email="mahmoudhousam60@gmail.com",
    description="Seamlessly integrates Plotly interactive visualizations into a single standalone HTML file offering a modern presentation-like experience with the flexibility of a web-based report",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MahmoudHousam/VizBlend",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "bs4==0.0.2",
        "plotly==6.1.1",
        "pytest==6.2.4",
        "pandas==2.2.3",
        "jinja2==3.1.4",
        "kaleido==1.0.0",
        "black==24.10.0",
        "python-pptx==1.0.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires=">=3.9",
)
