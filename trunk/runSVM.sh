#!/bin/bash
echo "compiling libSVM"
echo "================"
cd src/classification/svm/libsvm-2.91
make
cd python
make
echo "classification"
echo "=============="
echo "It takes about 5 minutes, please wait..."
python custom_svm.py
