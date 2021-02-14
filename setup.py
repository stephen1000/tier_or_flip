import setuptools

with open("readme.md", "r") as f:
    long_description = f.read()

dev_req = [
    "black==20.8b1",
    "pylint==2.6.0",
]

test_req = ["pytest==6.2.2", "pytest-cov==2.10.1"]

setuptools.setup(
    name="tier_or_flip",
    version="0.0.2",
    author="Stephen Lowery",
    author_email="author@example.com",
    description="Code used for a hearthstone helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    entry_points={"console_scripts": ["tier-or-flip = tier_or_flip.cli:handle"]},
    install_requires=[
        "python-dotenv==0.15.0",
        "requests==2.25.1",
    ],
    extras_require={
        "dev": test_req + dev_req,
        "test": test_req,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
