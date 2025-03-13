import os
import shutil

def configure_package_manager():
	package_manager = "{{ cookiecutter.package_manager }}"

	if package_manager == "poetry":
		# Replace the default pyproject.toml with the poetry version
		shutil.move("pyproject_poetry.toml", "pyproject.toml")
		
		# Remove setup.py since Poetry doesn't need it
		if os.path.exists("setup.py"):
			os.remove("setup.py")
	else:
		# If pip, just remove the unnecessary poetry_pyproject.toml file
		if os.path.exists("pyproject_poetry.toml"):
			os.remove("pyproject_poetry.toml")

if __name__ == "__main__":
	configure_package_manager()
