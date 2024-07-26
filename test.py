import os

API_KEY = "pypi-AgEIcHlwaS5vcmcCJDM4YjM0YWNiLTdiNzQtNGI5MS1iOTI1LTllMzE4NmQzMzg5NgACKlszLCI2M2RmODhmMy1jMzlmLTRiMDAtOTg1ZS1jNWJhZmRlZTFiZmUiXQAABiA32kI5Svm-hDKrIhj0n1bBFBfgIPP2GG0a7t4S_TGNiw"

os.system("del dist")
os.system("py -m build")
os.system("twine upload dist/* -p {}".format(API_KEY))