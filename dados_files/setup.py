import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]
cx_Freeze.setup(
    name="Dados System",
    options={'build_exe': {'packages': ['random'],
                           'include_files': []}},
    executables=executables
)
