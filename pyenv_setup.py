import os

# Enter .gitignore entries here:
gitignore_entries = [
    'pyenv_setup.py',
    '.log'
]

def one():

    # Initializing git repository

    try:
        print('\nStep 1: Initializing git repository..')
        os.system('git init')
    except:
        print('Step 1 failed')


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
    except:
        print('Task 3 failed')


    #

    try:
        print(' ')
        os.system(f'git config --global --add safe.directory "{os.getcwd().replace('\\', '/')}"')
    except:
        print('Task 3 failed')


    # Setting autocrlf in global config if not set already. 
    # To do: Check OS version

    try:
        print('\nSetting default line endings to autocrlf..')
        os.system('git config --global core.autocrlf true')
    except:
        print('Step failed.')


def two():

    # Staging all files
    try:
        print('\nStep 4: Staging files..\n')
        os.system('git config --global core.safecrlf false')            #DISABLE CRLF WARNINGS TEMPORARELY
        os.system('git add .')
        os.system('git config --global core.safecrlf true')             #RE-ENABLING CRLF WARNINGS
        #os.system('git status')                                        #GIT STATUS BEFORE COMMIT
    except:
        print('Step 4 failed')


    # Performing initial commit

    try:
        print('Step 5: Performing initial commit..\n')
        os.system('git commit -m "Environment setup."')
        os.system('git status')
    except:
        print('Step 5 failed')


def three():

    # Installing pip libraries

    try:
        print('\nInstalling pip libraries..')
        os.system('pip install -r "dependencies.txt"')
    except:
        print('Installation failed')


if __name__ == '__main__':

    print('\nThe script will create files at:')
    print(os.getcwd()+'\n')

    while True:
        proceed = input('Do you want to proceed with the setup?[y/n] ')
        if proceed == 'y':
            one()                    
            while True:
                print('\nReady to stage and commit the environment.')
                proceed = input('Continue?[y/n] ')
                if proceed =='y':
                    two()
                    while True:
                        print('\nReady to install pip dependencies.')
                        proceed = input('Continue?[y/n] ')
                        if proceed =='y':
                            three()
                            break
                        elif proceed == 'n':
                            break
                        else:
                            print('Please answer with "y" for YES or "n" for NO.')
                            break
                    break
                elif proceed == 'n':
                    break
                else:
                    print('Please answer with "y" for YES or "n" for NO.')
            break
        elif proceed == 'n':
            break
        else:
            print('Please answer with "y" for YES or "n" for NO.')

    
    # Asking for user input to enter Python virtual environment

    while True:
        answer = input('\nDo you want to enter the virtual environment?[y/n] ').lower()

        if answer == 'y':
            os.system('./Scripts/activate')
            break
        elif answer == 'n':
            os.system('deactivate')
        else:
            print('Please answer with "y" for YES or "n" for NO.')
    

