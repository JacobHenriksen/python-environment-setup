import os

# Enter .gitignore entries here:
gitignore_entries = [
    'pyenv_setup.py', 
    '.log'
]
dependencies_file = 'dependencies.txt'


def setup_process():
    print('\nThe script will create files in:')
    print(os.getcwd()+'\n')
    if user_prompt('Do you want to proceed with the setup?[Y/n] ') == 'y':
        proceed = part_one()
        print('\nReady to stage and commit the environment.')
        if user_prompt('Continue?[Y/n] ') == 'y' and proceed is True:
            proceed = part_two()
            print('\nReady to install pip dependencies.')
            if user_prompt('Continue?[Y/n] ') == 'y' and proceed is True:
                part_three()


def user_prompt(message):
    while True:
        response = input(message).lower()
        if response in ('','y', 'n'):
            if response in ('', 'y'):
                return 'y'
            elif response == 'n':
                return response
        else:
            print('Please answer with "y" for YES or "n" for NO.')


def part_one():

    # Initializing git repository
    try:
        print('\nStep 1: Initializing git repository..')
        os.system('git init')
    except Exception as e:
        print(f'Step 1 failed: {e}')
        return False

    # Creating .gitignore file and writing this script name to it
    with open(r'.gitignore', 'a') as gitignore:
        print('\nStep 2: Creating .gitignore and writing entries..')
        for entry in gitignore_entries:
            gitignore.write(entry)

    # Creating Python virtual environment
    try:
        print('Step 3: Creating Python Virtual Environment, please wait...')
        os.system('python -m venv .')
        print('Done.')
    except Exception as e:
        print(f'Step 3 failed: {e}')
        return False

    #
    try:
        print(' ')
        os.system(f'git config --global --add safe.directory "{os.getcwd().replace('\\', '/')}"')
    except Exception as e:
        print(f'Step ? failed: {e}')
        return False

    # Setting autocrlf in global config if not set already. 
    # To do: Check OS version
    try:
        print('\nSetting default line endings to autocrlf..')
        os.system('git config --global core.autocrlf true')
    except Exception as e:
        print(f'Step ? failed: {e}')
        return False
    else:
        return True


def part_two():

    # Staging all files
    try:
        print('\nStep 4: Staging files..\n')
        os.system('git config --global core.safecrlf false')            #DISABLE CRLF WARNINGS TEMPORARELY
        os.system('git add .')
        os.system('git config --global core.safecrlf true')             #RE-ENABLING CRLF WARNINGS
        #os.system('git status')                                        #GIT STATUS BEFORE COMMIT
    except Exception as e:
        print(f'Step 4 failed: {e}')
        return False

    # Performing initial commit
    try:
        print('Step 5: Performing initial commit..\n')
        os.system('git commit -m "Environment setup."')
        os.system('git status')
    except Exception as e:
        print(f'Step 5 failed: {e}')
        return False
    else:
        return True


def part_three():

    # Checking pip version and performing upgrade
    try:
        print(f'\nUpgrading pip package installer to the latest version..')
        os.system(f'python.exe -m pip install --upgrade pip')
    except Exception as e:
        print(f'Upgrade failed: {e}')
        return False

    # Installing pip libraries
    try:
        print(f'\nInstalling pip libraries from {dependencies_file}..')
        os.system(f'pip install -r "{dependencies_file}"')
    except Exception as e:
        print(f'Installation failed: {e}')
        return False
    else:
        return True
    

if __name__ == '__main__':

    setup_process()

    # Asking for user input to enter Python virtual environment
    while True:
        answer = input('\nDo you want to enter the virtual environment?[Y/n] ').lower()

        if answer in ('','y'):
            os.system('./Scripts/activate')
            break
        elif answer == 'n':
            os.system('deactivate')
        else:
            print('Please answer with "y" for YES or "n" for NO.')        

