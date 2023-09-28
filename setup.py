import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='spam_patterns',
    version='0.0.1',
    author='Devin Cowan',
    author_email='dcowan@cuahsi.org',
    description='Common spam patterns for shared CUAHSI services',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/CUAHSI/spam_patterns',
    project_urls={"Bug Tracker": "https://github.com/CUAHSI/spam_patterns/issues"},
    license='MIT',
    packages=['spam_patterns'],
    install_requires=[],
)
