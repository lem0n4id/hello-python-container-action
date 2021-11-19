import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYINPUT"]

    my_output = f"Hello {my_input}"

    # "::" is a special syntax to run the workflow commands.
    # https://docs.github.com/en/actions/learn-github-actions/workflow-commands-for-github-actions#using-workflow-commands-to-access-toolkit-functions
    print(f"::set-output name=myOutput::{my_output}")
    print("hello world!")


if __name__ == "__main__":
    main()
