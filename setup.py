from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of non-empty, stripped lines.

    Args:
      file_path (str): The path to the requirements file.

    Returns:
      List[str]: A list of requirements as strings. If the file is not found,
             an empty list is returned and an error message is printed.

    Raises:
      FileNotFoundError: If the specified file does not exist (handled internally).
    """

    try:
        with open(file_path) as file:
            requirements = file.readlines()
            requirements = [req.strip() for req in requirements if req.strip()]
            
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
                
        return requirements
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []


setup(
    name="mlproject",
    version="0.0.1",
    author="Juan Mario Parra 2025",
    author_email="jmparra.dev@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
