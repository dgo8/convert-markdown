from setuptools import setup, find_packages

setup(
    name="exportmd",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "markdown>=3.3.0",
        "beautifulsoup4>=4.9.0",
        "plotly>=5.0.0",
        "matplotlib>=3.4.0",
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "python-pptx>=0.6.0",
        "pdf2docx>=0.5.0",
        "weasyprint>=54.0",
        "seaborn>=0.11.0",
        "kaleido>=0.2.0"
    ],
) 