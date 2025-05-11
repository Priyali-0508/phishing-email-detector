from setuptools import setup, find_packages

setup(
    name="phishing_email_detector",
    version="1.0.0",
    author="Priyali Poojari",
    description="Phishing email detection using TF-IDF and Random Forest",
    packages=find_packages(),
    install_requires=[
        "pandas==2.2.3",
        "scikit-learn==1.6.1",
        "joblib==1.4.2"
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
