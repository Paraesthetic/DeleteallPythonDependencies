# Copyright 2026 Ex.perdition Software
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may use this file only in compliance with the License.
# A copy of the License is provided in the LICENSE file distributed with this code.
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

import pkg_resources
import subprocess
import sys

def main():
    # Packages to exclude from uninstallation
    exclude_packages = {'pip', 'setuptools', 'wheel'}

    # Retrieve a list of all installed packages
    installed_packages = [dist.project_name for dist in pkg_resources.working_set 
                          if dist.project_name not in exclude_packages]
    
    # Display the list of installed packages
    print("The following packages are installed:")
    for package in installed_packages:
        print(f"- {package}")

    # Confirm uninstallation
    confirm = input("\nAre you sure you want to uninstall all these packages? (yes/no): ")
    if confirm.lower() != 'yes':
        print("Operation cancelled.")
        sys.exit()

    # Uninstall each package
    for package in installed_packages:
        print(f"Uninstalling {package}...")
        subprocess.call([sys.executable, '-m', 'pip', 'uninstall', '-y', package])

    print("\nAll specified packages have been uninstalled.")

if __name__ == '__main__':
    main()
