from setuptools import setup, find_packages

setup(
name='scqgenerator',
version='0.0.1',
author='ritik gupta',
author_email='guptaritik67856@gamil.com' ,
install_requires = ["openai",
"langchain",
"streamlit",
"python-dotenv",
"PyPDF2"]   ,
packages = find_packages()
)
