# -*- mode: python -*-
a = Analysis(['mac_conversion.py'],
             pathex=['/home/dintorf/Developer/CSE469Project/cse469-cweinhold-dintorf-project/mac_conversion'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mac_conversion',
          debug=False,
          strip=None,
          upx=True,
          console=True )
