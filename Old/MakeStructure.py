# Let's create a Python script to generate the folder structure and files for the project.

import os

# Define the project structure
project_structure = {
    'your_project': {
        'app': {
            '__init__.py': '',
            'config.py': '',
            'models.py': '',
            'routes.py': '',
            'openai_integration.py': '',
            'utils.py': '',
            'errors.py': '',
            'schemas.py': '',
        },
        'migrations': {},
        'tests': {
            '__init__.py': '',
            'test_config.py': '',
            'test_models.py': '',
            'test_api.py': '',
        },
        '.env': '',
        '.flaskenv': '',
        '.gitignore': '',
        'requirements.txt': '',
        'setup.py': '',
        'README.md': '',
        'main.py': '',
    }
}

# Function to create directories and files based on the provided structure
def create_structure(base_path, structure):
    for name, value in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(value, dict):
            # It's a directory
            os.makedirs(path, exist_ok=True)
            create_structure(path, value)  # Recursively create subdirectories/files
        else:
            # It's a file
            with open(path, 'w') as f:
                f.write(value)  # Create an empty file or with predefined content

# Create the folder structure starting from the current directory
create_structure('.', project_structure)

# Return a list of files and folders created
created_paths = []
for root, dirs, files in os.walk('./your_project', topdown=True):
    for name in dirs:
        created_paths.append(os.path.join(root, name))
    for name in files:
        created_paths.append(os.path.join(root, name))

created_paths.sort()
created_paths
