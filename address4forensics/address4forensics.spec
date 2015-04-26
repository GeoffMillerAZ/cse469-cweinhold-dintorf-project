# -*- mode: python -*-
a = Analysis(['address4forensics.py'],
             pathex=['/Users/dintorf/Developer/School/CSE469/Project/cse469-cweinhold-dintorf-project/address4forensics'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='address4forensics',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='address4forensics')
