# -*- mode: python -*-
a = Analysis(['mac_conversion.py'],
             pathex=['/home/dintorf/Developer/CSE469Project/cse469-cweinhold-dintorf-project/mac_conversion'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='mac_conversion',
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
               name='mac_conversion')
