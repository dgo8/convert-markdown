from setuptools import setup, find_packages

setup(
    name="ExportMd",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "markdown",
        "weasyprint",
        "beautifulsoup4",
        "python-pptx",
        "pdf2docx",
        "plotly",
        "matplotlib",
        "numpy",
        "pandas",
        "seaborn"
    ],
) 