import subprocess
rc = 4
while rc == 4:
    h=subprocess.run(["python3","newo.py"])
    rc = h.returncode
