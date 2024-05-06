# GOPEM Release Instructions

**Last Update: 2024-05-07**

1. Create the `release` branch under `develop`
2. Update all version tags
	1. `setup.py`
	2. `README.md`
	3. `SECURITY.md`
	4. `GOPEM.spec`
	5. `GOPEM.iss`
	6. `gopem/helper.py`
	7. `rsrc/version_check.py`
	8. `rsrc/Version.rc`
3. Update `CHANGELOG.md`
	1. Add a new header under `Unreleased` section (Example: `## [0.1] - 2022-08-17`)
	2. Add a new compare link to the end of the file (Example: `[0.2]: https://github.com/ECSIM/gopem/compare/v0.1...v0.2`)
	3. Update `develop` compare link (Example: `[Unreleased]: https://github.com/ECSIM/gopem/compare/v0.2...develop`)
4. Update `.github/ISSUE_TEMPLATE/bug_report.yml`
   1. Add new version tag to `GOPEM version` dropbox options
5. Create a PR from `release` to `develop`
	1. Title: `Version x.x` (Example: `Version 0.1`)
	2. Tag all related issues
	3. Labels: `release`
	4. Set milestone
	5. Wait for all CI pass
	6. Need review (**1** reviewer)
	7. Squash and merge
	8. Delete `release` branch
6. Merge `develop` branch into `master`
	1. `git checkout master`
	2. `git merge develop`
	3. `git push origin master`
	4. Wait for all CI pass
7. Build EXE files (Windows)
	1. Update `OPEM` version to the latest version available on [PyPI](https://pypi.org/project/opem/)
		1. `build_script.exe`
	2. Run `build_exe.bat` (Use `Python >= 3.6`)
	3. Run `GOPEM.iss` (Use `Inno Setup >= 6.0.2`)
8. Create a new release
	1. Target branch: `master`
	2. Tag: `vx.x` (Example: `v0.1`)
	3. Title: `Version x.x` (Example: `Version 0.1`)
	4. Copy changelogs
	5. Tag all related issues
	6. Upload `dist/GOPEM-x.x.exe`
	7. Upload `dist/GOPEM-Portable-x.x.exe`
9. Bump!!
10. Close this version issues
11. Close milestone
12. Update website
	1. `git checkout gh-pages`
	2. Update `index.html` page
		1. Add a new section
		2. Add changelogs
		3. Add download links
	3. Update `update.html`
	4. `git push origin gh-pages`