# ft_package

A sample Python package containing a `count_in_list` function.

## Building Distribution

python3 -m build

## How to Test
If it doesn't exist, create a tester.py outside ex09, with the script from the subject https://cdn.intra.42.fr/pdf/pdf/211089/en.subject.pdf. \
To test installation both ways, create a venv and enter
- python3 -m venv venv
- source venv/bin/activate

Check if you entered venv corectly 
- which python

It should display something with:
- ex09/venv

Test both installations :
- pip install ./dist/ft_package-0.0.1.tar.gz
- pip install ./dist/ft_package-0.0.1-py3-none-any.whl

seperatly by doing:
- install
- pip show -v ft_package (also see installed package inside venv/lib/...)
- python3 ../tester.py
- pip uninstall ft_package 
- repeat with other installation
- deactivate
- rm -rf venv
