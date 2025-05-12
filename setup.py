from setuptools import setup, find_packages

setup(
    name='pharma-ai-visibility-intelligence',
    version='0.1.0',
    description='Strategic AI Visibility Intelligence Platform for Pharmaceutical Brands',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='AI Visibility Intelligence Team',
    author_email='contact@pharma-ai-intelligence.com',
    packages=find_packages(),
    install_requires=[
        'streamlit>=1.34.0',
        'pandas>=2.2.1',
        'plotly>=5.20.0',
        'numpy>=1.26.4',
        'seaborn>=0.12.2',
        'matplotlib>=3.7.1'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Pharmaceutical Companies',
        'Topic :: Scientific/Engineering :: Medical Science Apps',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    keywords='pharmaceutical ai visibility intelligence marketing',
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'pharma-ai-visibility=app:main',
            'generate-mock-data=mock_data_generator:main',
            'analyze-visibility=data_analysis:main'
        ]
    }
)
