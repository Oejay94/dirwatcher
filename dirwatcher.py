import os
import argparse
import time
import datetime
import logging
import signal
import sys
_author_ = "Joey with help from demo videos and coaches"

if sys.version_info[0] < 3:
    raise RuntimeError("This program requires Python 3")

"""Global Variables"""
logger = logging.getLogger(__file__)
exit_flag = False
watch_files = {}
last_position = 0


def watch_directory(args):
    """Watches directory for magic text"""
    directory = args.path
    # logger.info('Watch Dir: {}, File Ext: {}, Polling Int: {}, Magic Txt: {}'
    #             .format(directory, args.ext, args.interval, args.magic))

    file_list = [os.path.join(directory, f)
                 for f in os.listdir(directory)]
    for file in file_list:
        if file not in watch_files and file.endswith(args.ext):
            watch_files[file] = 0
            logger.info('Watching new file: {}'.format(file))
    for file in list(watch_files):
        if file not in file_list:
            logger.info('Removed deleted file: {}'.format(file))
            del watch_files[file]
    for file in watch_files:
        last_line_num = find_magic(
            file, watch_files[file], args.magic)
        watch_files[file] = last_line_num
    time.sleep(args.interval)


def find_magic(filename, skip_to_line, magic_word):
    """
    Read a file and looks for a magic text
    while logging a message if found.
    """
    i = 0
    with open(filename) as f:
        for i, line in enumerate(f, start=1):
            if i < skip_to_line:
                continue
            if magic_word in line:
                logger.info(f'Found the {magic_word} on {i} in {filename}')
        return i + 1


def create_parser():
    """Creates and returns an argparse cmd line"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--ext', type=str, default='.txt',
                        help='Text file extension to watch')
    parser.add_argument('-i', '--interval', type=float, default=1.0,
                        help='How often to watch the text file')
    parser.add_argument('path', help='Directory to watch')
    parser.add_argument('magic', help='String to watch for')
    return parser


def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT.
    Other signals can be mapped here as well (SIGHUP?)
    Basically it just sets a global flag,
    and main() will exit it's loop if the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    global exit_flag
    logger.warning('Received ' + signal.Signals(sig_num).name)
    if sig_num == signal.SIGINT or signal.SIGTERM:
        exit_flag = True


def main():
    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d %(name)-12s %(levelname)-8s'
        '[%(threadName)-12s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger.setLevel(logging.DEBUG)
    app_start_time = datetime.datetime.now()
    logger.info(
        '\n'
        '----------------------------------------------------\n'
        '   Running {0}\n'
        '   Started on {1}\n'
        '----------------------------------------------------\n'
        .format(__file__, app_start_time.isoformat())
    )
    parser = create_parser()
    args = parser.parse_args()
    uptime = datetime.datetime.now() - app_start_time
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    logger.info('Watch Dir: {}, File Ext: {}, Polling Int: {}, Magic Txt: {}'
                .format(args.path, args.ext, args.interval, args.magic))

    while not exit_flag:
        try:
            watch_directory(args)
        except OSError as e:
            logger.error(e)
        except Exception as e:
            logger.exception('Unhandled exception: {}'.format(e))
        time.sleep(args.interval)

    logger.info(
        '\n'
        '----------------------------------------------------\n'
        '   Stopped {0}\n'
        '   Uptime was {1}\n'
        '----------------------------------------------------\n'
        .format(__file__, str(uptime))
    )


if __name__ == '__main__':
    main()
