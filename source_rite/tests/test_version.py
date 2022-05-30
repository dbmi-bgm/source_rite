import os

from dcicutils.qa_utils import VersionChecker


def test_version_consistency():

    class MyVersionChecker(VersionChecker):

        _ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

        PYPROJECT = os.path.join(_ROOT_DIR, "pyproject.toml")
        CHANGELOG = os.path.join(_ROOT_DIR, "CHANGELOG.rst")

    print(f"pyproject file = {MyVersionChecker.PYPROJECT}")
    print(f"changelog file = {MyVersionChecker.CHANGELOG}")

    MyVersionChecker.check_version()
