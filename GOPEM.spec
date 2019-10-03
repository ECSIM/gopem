# -*- mode: python -*-

block_cipher = None


a = Analysis(['gopem/__main__.py'],
             pathex=['gopem'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=["nbconvert","nbformat","notebook","psutil"],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
		  a.scripts,
		  exclude_binaries=True,
          name='GOPEM',
          debug=False,
          strip=False,
          upx=True,
		  icon='rsrc/icon.ico',
		  version="rsrc/Version.rc",
          console=True )

exe2 = EXE(pyz,
		  a.scripts,
		  a.binaries,
          a.zipfiles,
          a.datas,
          name='GOPEM',
          debug=False,
          strip=False,
          upx=True,
		  icon='rsrc/icon.ico',
		  version="rsrc/Version.rc",
          console=True )

coll = COLLECT(exe,
          a.binaries,
          a.zipfiles,
          a.datas,
		  strip=False,
          upx=True,
		  name='GOPEM')
