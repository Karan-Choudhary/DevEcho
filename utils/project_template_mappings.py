TEMPLATE_MAPPINGS = {
    'general_project': {
        'directories': ['src', 'utils'],
        'files': ['src/main.py', 'utils/sample.py'],
    },
    'ml_project': {
        'directories': ['src', 'Dataset', 'Experiments', 'Models', 'Result', 'utils'],
        'files': ['params.yaml', 'src/main.py', 'Experiments/EXP1.ipynb', 'utils/sample.py']
    },
}

BOILER_CODE = {
    "python": {
        "main.py": "utils/boilerplate/python_main.txt",
        "sample.py": "utils/boilerplate/util_sample.txt" 
    }
}