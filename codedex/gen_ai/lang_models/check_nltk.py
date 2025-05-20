# Check if the numpy and nltk is installed:

try:
    import numpy
    print("NumPy is installed. Version:", numpy.__version__)
except ImportError:
    print("NumPy is NOT installed.")

try:
    import nltk
    print("NLTK is installed. Version:", nltk.__version__)
except ImportError:
    print("NLTK is NOT installed.")


