import sys
import argparse
from midterm import app

# APPLICATION TIER - Executable file
# = Parses the argument of port and uses it run the application

def main():
    # Step 1: import argparse and add arguments. Common argument is port.
    
    # Parse the arguments
    parser = argparse.ArgumentParser(description="An object slideshow application.", 
                                     allow_abbrev=False)
    
    parser.add_argument('port',help='the port at which the server should listen')
    args = parser.parse_args()
    
    # Step 2: get the port number from the arguments, cast to int and store at variable port    
    try:
        port = int(args.port)
    except Exception:
        print('Port must be an integer.', file=sys.stderr)
        exit(1)
    
    # Step 3: run the application imported from another file midterm.py
    try:
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as ex:
        print(ex, file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    main()