# -*- mode: python -*-
a = Analysis(['address4forensics.py'],
             pathex=['/home/dintorf/Developer/CSE469Project/cse469-cweinhold-dintorf-project/address4forensics'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='address4forensics',
          debug=False,
          strip=None,
          upx=True,
          console=True )
