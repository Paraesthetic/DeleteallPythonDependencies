# Python Environment Package Cleaner

Remove almost every third party package from the currently active Python environment and return it to a minimal state.

This utility is intended for disposable virtual environments that have accumulated conflicting, unnecessary or experimental packages. It lists the packages it intends to remove, requires an exact confirmation and then uninstalls each package through the active Python interpreter.

> [!WARNING]
> This is deliberately destructive. Do not run it against a system Python installation, a shared environment or an environment that cannot be recreated. Export the environment or keep its requirements file before proceeding.

## What it removes

The script reads installed distributions from the active Python environment and removes each one except:

* pip
* setuptools
* wheel

It does not uninstall Python itself, standard library modules, operating system packages or packages installed in a different Python environment.

## Appropriate uses

* Resetting a temporary virtual environment.
* Clearing dependencies before rebuilding from a known requirements file.
* Recovering a test environment affected by package conflicts.
* Removing packages from an environment created for a one off experiment.

## Recommended safe workflow

Create and activate a virtual environment, install a few disposable packages and test the script there before using it elsewhere.

On Windows:

    python -m venv test_environment
    test_environment\Scripts\activate
    python -m pip freeze > packages_before_cleanup.txt
    python "Python - Rm all plugins.py"

On macOS or Linux:

    python3 -m venv test_environment
    source test_environment/bin/activate
    python -m pip freeze > packages_before_cleanup.txt
    python "Python - Rm all plugins.py"

The script prints every package selected for removal and asks:

    Are you sure you want to uninstall all these packages? (yes/no):

Only the exact response yes continues. Any other response cancels the operation.

## Verify the target environment

Before confirming, check that the Python executable belongs to the intended virtual environment:

    python -c "import sys; print(sys.executable)"

After completion, review what remains:

    python -m pip list

## Limitations

* Packages are removed one at a time, so a large environment may take some time.
* An interrupted run can leave the environment only partly cleaned.
* Uninstall failures are not collected into a final failure report.
* The script does not recreate packages or preserve version information unless you export it first.
* The package discovery method depends on pkg_resources from setuptools.

## Licence

GNU General Public License version 3. See LICENSE for the complete terms.
