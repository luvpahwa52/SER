import os

def create_directory_structure(project_name):
    # Define the directory structure of the ML project
    directories = [
        'data/raw',
        'data/processed',
        'data/interim',
        'models/trained_models',
        'models/model_evaluation',
        'notebooks',
        'src/data',
        'src/models',
        'src/utils',
        'tests'
    ]

    # Create directories
    for directory in directories:
        os.makedirs(os.path.join(project_name, directory), exist_ok=True)

    # Create __init__.py files for each package
    for root, dirs, files in os.walk(project_name):
        for dir in dirs:
            init_file = os.path.join(root, dir, '__init__.py')
            # Check if __init__.py already exists
            if not os.path.exists(init_file):
                with open(init_file, 'w') as f:
                    pass

    # Create a main.py file in src directory if it doesn't exist
    main_file = os.path.join(project_name, 'src', 'main.py')
    if not os.path.exists(main_file):
        with open(main_file, 'w') as f:
            f.write('# Main script')

    # Create a requirements.txt file if it doesn't exist
    requirements_file = os.path.join(project_name, 'requirements.txt')
    if not os.path.exists(requirements_file):
        with open(requirements_file, 'w') as f:
            pass

    # Create a README.md file if it doesn't exist
    readme_file = os.path.join(project_name, 'README.md')
    if not os.path.exists(readme_file):
        with open(readme_file, 'w') as f:
            f.write('# ' + project_name + '\n\nDescription of the project.')

    # Create a .gitignore file if it doesn't exist
    gitignore_file = os.path.join(project_name, '.gitignore')
    if not os.path.exists(gitignore_file):
        with open(gitignore_file, 'w') as f:
            f.write('*.pyc\n__pycache__/\n')

    # Print message to confirm project structure creation
    print(f"Project structure created for '{project_name}'.")

if __name__ == "__main__":
    # Prompt user to input project name
    project_name = input("Enter the name of the project: ")

    # Call function to create directory structure
    create_directory_structure(project_name)
