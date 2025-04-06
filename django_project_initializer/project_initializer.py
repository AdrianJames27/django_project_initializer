import os, stat, subprocess, shutil, sys

def remove_readonly(func, path, exc_info):
    """
    Error handler for shutil.rmtree.

    Clears the readonly bit and reattempts removal.
    """
    os.chmod(path, stat.S_IWRITE)  # Add write permission
    func(path)

def prompt_for_project_name():
    project_name = input("Enter the project name: ")
    return project_name.strip()

def clone_repository(project_name):
    repo_url = "https://github.com/AdrianJames27/django_template.git"
    clone_dir = project_name
    subprocess.run(["git", "clone", "--depth", "1", "--branch", "master", repo_url, clone_dir])
    return clone_dir

def remove_git_directory(clone_dir):
    git_dir = os.path.join(clone_dir, ".git")
    if os.path.exists(git_dir):
        shutil.rmtree(git_dir, onexc=remove_readonly)

def rename_project_directory(clone_dir, project_name):
    os.rename(clone_dir, project_name)

def main():
    try:
        project_name = prompt_for_project_name()
        clone_dir = clone_repository(project_name)
        remove_git_directory(clone_dir)
        rename_project_directory(clone_dir, project_name)
        
        # Rich text format instructions
        print(f"\nProject '{project_name}' has been initialized successfully.")
        print("\nNext steps:")
        print(f"1. Change directory to your project:")
        print(f"   cd {project_name}")
        print(f"2. Activate the virtual environment:")
        print("   pipenv shell")
        print(f"3. Install the required packages:")
        print("   pipenv install -r requirements.txt")

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
        sys.exit(0)
    except EOFError:
        print("\nInput ended. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}. Exiting...")
        sys.exit(1)

if __name__ == "__main__":
    main()
