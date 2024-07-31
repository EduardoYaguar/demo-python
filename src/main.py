import os

num = os.environ.get("INPUT_NUM")
if num:
    try:
        num = int(num)
    except Exception:
        exit("El número ingresado no es entero")
else:
    num = 1

if "GITHUB_OUTPUT" in os.environ:
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        print("{0}={1}".format("result", num+3), file=f)
