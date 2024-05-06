# -*- coding: utf-8 -*-
"""Version-check script."""
import os
import sys
import codecs
Failed = 0
VERSION = "0.8"

VERSION_1 = VERSION.split(".")[0]
VERSION_2 = str(int(float(VERSION) * 10 - int(VERSION_1) * 10))
VERSION_3 = str(int(float(VERSION) * 100 - int(VERSION_1)
                    * 100 - int(VERSION_2) * 10))
VERSION_4 = "0"

SETUP_ITEMS = [
    "version='{0}'",
    'https://github.com/ecsim/gopem/tarball/v{0}']
INSTALL_ITEMS = [
    "[Version {0}](https://github.com/ecsim/gopem/archive/v{0}.zip)",
    "[Installer-Version {0}](https://github.com/ECSIM/gopem/releases/download/v{0}/GOPEM-{0}.exe)",
    "[Portable-Version {0}](https://github.com/ECSIM/gopem/releases/download/v{0}/GOPEM-Portable-{0}.exe)",
    "pip install gopem=={0}"]
CHANGELOG_ITEMS = [
    "## [{0}]",
    "https://github.com/ECSIM/gopem/compare/v{0}...develop",
    "[{0}]:"]
HTML_ITEMS = ["Version {0}"]
PARAMS_ITEMS = ["Version = {0}"]
RC_ITEMS = [
    "filevers=({0}, {1}, {2}, {3})",
    "prodvers=({0}, {1}, {2}, {3})",
    "(u'FileVersion', u'{0}.{1}.{2}.{3}'),",
    "(u'ProductVersion', u'{0}, {1}, {2}, {3}')"]
TEST_ITEMS = ["New Version ({0}) Is Available!"]
INNO_ITEMS = ['#define MyAppVersion "{0}"']
SPEC_ITEMS = ['gopem_version = "{0}"']
ISSUE_TEMPLATE_ITEMS = ["- GOPEM {0}"]
SECURITY_ITEMS = ["| {0}           | :white_check_mark: |", "| < {0}         | :x:                |"]
FILES = {
    "setup.py": SETUP_ITEMS,
    "README.md": INSTALL_ITEMS,
    "CHANGELOG.md": CHANGELOG_ITEMS,
    "SECURITY.md": SECURITY_ITEMS,
    os.path.join(
        "gopem",
        "helper.py"): PARAMS_ITEMS,
    "GOPEM.iss": INNO_ITEMS,
    "GOPEM.spec": SPEC_ITEMS,
    os.path.join(".github", "ISSUE_TEMPLATE", "bug_report.yml"): ISSUE_TEMPLATE_ITEMS,
    }

TEST_NUMBER = len(FILES) + 1


def print_result(failed=False):
    """
    Print final result.

    :param failed: failed flag
    :type failed: bool
    :return: None
    """
    message = "Version tag tests "
    if not failed:
        print("\n" + message + "passed!")
    else:
        print("\n" + message + "failed!")
    print("Passed : " + str(TEST_NUMBER - Failed) + "/" + str(TEST_NUMBER))


if __name__ == "__main__":
    for file_name in FILES:
        try:
            file_content = codecs.open(
                file_name, "r", "utf-8", 'ignore').read()
            for test_item in FILES[file_name]:
                if file_content.find(test_item.format(VERSION)) == -1:
                    print("Incorrect version tag in " + file_name)
                    Failed += 1
                    break
        except Exception as e:
            Failed += 1
            print("Error in " + file_name + "\n" + "Message : " + str(e))
    try:
        file_content = codecs.open(
            os.path.join(
                "rsrc",
                "Version.rc"),
            "r",
            "utf-8",
            'ignore').read()
        for test_item in RC_ITEMS:
            if file_content.find(
                test_item.format(
                    VERSION_1,
                    VERSION_2,
                    VERSION_3,
                    VERSION_4)) == -1:
                print("Incorrect version tag in " + "Version.rc")
                Failed += 1
                break
    except Exception as e:
        Failed += 1
        print("Error in Version.rc" + "\n" + "Message : " + str(e))
    if Failed == 0:
        print_result(False)
        sys.exit(0)
    else:
        print_result(True)
        sys.exit(1)
