import sys
import app
import flask

def main():
    try:
        app.app.run(host="0.0.0.0", port=55556, debug=True)

    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)
        
if __name__ == "__main__":
    main()