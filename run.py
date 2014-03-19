import logging
import argparse

from app import app


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="flask boilerplate")
    parser.add_argument('-d', '--debug', dest='debug', default=True,
                        help='Enable debugging mode.')
    parser.add_argument('-p', '--port', dest='port', default=8000, type=int,
                        help='Port to listen on.')
    args = parser.parse_args()

    loglevel = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=loglevel)

    print 'Starting application...'
    app.run(host='127.0.0.1', port=args.port, debug=args.debug)
