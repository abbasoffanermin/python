import subprocess

def run_main():
    try:
        subprocess.run(["python", "C:\\Users\\Narmin\\Desktop\\RedRab\\tests\\test1.py"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error running main.py:", e)

if __name__ == "__main__":
    run_main()
