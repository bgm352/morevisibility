from setuptools import setup, find_packages

setup(
    name='pharma_ai_visibility',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'pandas',
        'numpy',
        'plotly',
        'matplotlib',
        'seaborn',
        'scipy'
    ],
    entry_points={
        'console_scripts': [
            'pharma-ai-visibility=pharma_ai_visibility.app:main',
        ]
    }
)
