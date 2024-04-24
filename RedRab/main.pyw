import subprocess
from time import sleep

program_path = "C:\\Users\\Narmin\\Desktop\\RedRab\\beta1.pyw"

def run_main():
    try:
        subprocess.run(["python", program_path], check=True)
    except subprocess.CalledProcessError as e:
        print("Error running beta1.pyw:", e)

run_main()


counter = 0

while True:

    if counter == 10:
        break

    else:
        sleep(3600)
        run_main()
        counter += 1
        

