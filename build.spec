# -*- mode: python ; coding: utf-8 -*-

import os
import sys
sys.setrecursionlimit(sys.getrecursionlimit() * 5)

block_cipher = None

# 分析需要包含的模块
a = Analysis(
    ['gui.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('version.py', '.'),
    ],
    hiddenimports=[
        'bs4',
        'fake_useragent',
        'tqdm',
        'requests',
        'urllib3',
        'ebooklib',
        'PIL',
        'PIL.Image',
        'PIL.ImageTk',
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'tkinter.filedialog',
        'tkinter.font',
        'tkinter.scrolledtext',
        'threading',
        'json',
        'os',
        'sys',
        'time',
        're',
        'base64',
        'gzip',
        'urllib.parse',
        'concurrent.futures',
        'collections',
        'typing',
        'signal',
        'random',
        'io'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'pandas',
        'numpy',
        'scipy',
        'bokeh',
        'h5py',
        'lz4',
        'jinja2',
        'cloudpickle',
        'dask',
        'distributed',
        'fsspec',
        'pyarrow',
        'pytz'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='TomatoNovelDownloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # 禁用UPX压缩以避免Windows构建问题
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # 设置为窗口模式
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
) 