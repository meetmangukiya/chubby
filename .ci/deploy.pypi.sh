set -e

echo "Uploading chubby to PyPI"

if [[ -z "$CHUBBY_ROOT" ]]; then
else
    cd $CHUBBY_ROOT
fi

version_number=`cat chubby/VERSION`
new_version=`python3 -c "from chubby.version import generate_dev_version;print(generate_dev_version('$version_number'))"`

echo $new_version > chubby/VERSION

pip3 install twine wheel
python3 setup.py sdist bdist_wheel
# Upload one by one to avoid timeout
twine upload dist/* -u "$PYPIUSER" -p "$PYPIPW" 2>&1 | tee twine_output.txt
if [ "${PIPESTATUS[0]}" -ne 0 ]; then
    SEARCH_STR="500 Server Error"
    if grep -q "$SEARCH_STR" twine_output.txt; then
        echo "Server error 500"
        exit 1
    fi
fi
rm twine_output.txt

echo "Installing chubby from pypi"
pip3 install --pre chubby --upgrade
