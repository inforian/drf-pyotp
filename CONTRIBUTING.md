# Contributing to Readme Markdown Generator

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.
Please note we have a [code of conduct](https://github.com/inforian/drf-pyotp/tree/master/.github/CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Table of Contents

- [Setting Up the project locally](#setting-up-the-project-locally)
- [Submitting a Pull Request](#submitting-a-pull-request)

## Setting Up the project locally

To install the project you need to have `python` and `pip` installed

1.  [Fork](https://help.github.com/articles/fork-a-repo/) the project, clone
    your fork:

    ```sh
    # Clone your fork
    git clone https://github.com/<your-username>/drf-pyotp.git

    # Navigate to the newly cloned directory
    cd drf-pyotp
    ```

2.  From the root of the project create a virtual environment
    - For python 2:
    ```sh
    #install the virtualenv package using pip
    pip install virtualenv

    # create the virtual environment
    virtualenv env
    ```
    - For python 3:
    ```sh
    # create the virtualenv
    python3 -m venv env

    ```


3.  from the root of the project: `pip install -r requirements` to install all dependencies

    - make sure you have latest `pip` version

4.  from the root of the project: `python manage.py runserver` to run the project.

> Tip: Keep your `master` branch pointing at the original repository and make
> pull requests from branches on your fork. To do this, run:
>
> ```sh
> git remote add upstream https://github.com/inforian/drf-pyotp.git
> git fetch upstream
> git branch --set-upstream-to=upstream/master master
> ```
>
> This will add the original repository as a "remote" called "upstream," then
> fetch the git information from that remote, then set your local `master`
> branch to use the upstream master branch whenever you run `git pull`. Then you
> can make all of your pull request branches based on this `master` branch.
> Whenever you want to update your version of `master`, do a regular `git pull`.

## Submitting a Pull Request

Please go through existing issues and pull requests to check if somebody else is already working on it.

Also, make sure to run the tests and lint the code before you commit your
changes.


