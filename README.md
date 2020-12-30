# Python CLI Template

This is a template project for creating a Python CLI app intended for distribution to PyPI (so that you can `pip install` it later). It currently uses `Python 3.8` and has been developed/tested on Ubuntu.

* 📦 Easily create a Python app that is distributed to [PyPI](https://pypi.org/) and can be installed by anyone with `pip install`. 
* :computer: ​The package is configured with a `script`, so you can run it directly from a terminal once installed. 
* ✅ Added sample tests with `pytest` so you can keep your package well tested! 
* :100: Automatic version increment.

## Configuration

To configure the project, modify `publish/config.json`:

```bash
vi publish/config.json
```

Here is the default sample configuration:

```json
{
  "author": "Pixegami",
  "package_name_override": "pixegami-my-app",
  "email": "pixegami@gmail.com",
  "description": "A template Python CLI app.",
  "url": "https://github.com/pixegami/python-cli-template",
  "python_version": "3.8",
  "version": "0.0.8",
  "scripts": [
    "run-my-app = my_app:main"
  ]
}
```

This will be the information that is published to PyPI. Your `scripts` array allows you to specify which commands will be available once you install this package. 

For example, this configuration will let you execute `run-my-app` as a command directly from terminal, which will call the `main()` function in the `my_app` package.

The `package_name_override` will be what we attempt to publish the package as, so make sure it is unique on PyPI.

## Publish Locally

This will build the package, and install it directly into your current Python environment.

```bash
cd publish
sh ./publish_local.sh
```

Once installed, you should be able to test the script.

```bash
run-my-app
# Executing 'main()' from my app!
# Hello World

run-my-app --version 
# Executing 'main()' from my app!
# 0.0.7
```

## Publish to PyPI

First, you will need to [create an account on PyPI](https://pypi.org/account/register/). Then you need to export your PyPI credentials in the environment variables of your terminal.

I like to do this by just adding the following exports to the `~/.bashrc` (or whichever file, depending on the terminal you are using).

```bash
export PYPI_REPO_USER="YOUR_USERNAME"
export PYPI_REPO_PASS="YOUR_PASSWORD"
```

The publish script will use these environment variables to upload your package to PyPI. Next, you can run the script:

```bash
cd publish
sh ./publish_remote.sh
```

This will build it into a package like so: https://pypi.org/project/pixegami-my-app/. Now you can install it directly with `pip install`.

## Testing

To run the tests, you need to install `pytest`, which is already in the `developer_requirements.txt`.

```bash
pip install pytest
```

From the project root, you can run this to test and print all output:

```bash
python -m pytest -s
```

Or to test a specific file or function:

```bash
# Test file tests/test_my_app.py
python -m pytest -s tests/test_my_app.py

# Test function test_app_main() in tests/test_my_app.py
python -m pytest -s tests/test_my_app.py::test_app_main
```

## Versioning

Every time you publish the package (either locally or remote), the `version` field in `publish/config.json` will go up (specifically, the last digit). So `1.2.3` will become `1.2.4`, etc. It will keep going up.

The major and minor versions (the first two digits) can only be changed manually. Change it directly in the file when you need to.

## Related Reading

* [Packaging Python projects](https://packaging.python.org/tutorials/packaging-projects/): A guide explaining how to package Python projects using `setup.py` and `setuptools` (we use this here).
* [argparse](https://docs.python.org/3/library/argparse.html): I use this to "understand" CLI arguments and sub-commands.
* [pytest](https://docs.pytest.org/en/stable/): Testing framework for this project.