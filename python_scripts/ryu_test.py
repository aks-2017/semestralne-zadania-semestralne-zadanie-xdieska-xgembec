import sys

from ryu.cmd import manager


def main():
    sys.argv.append('--ofp-tcp-listen-port')
    sys.argv.append('6633')
    sys.argv.append('simple_switch_13')
    sys.argv.append('--verbose')
    sys.argv.append('--enable-debugger')
    manager.main()

if __name__ == '__main__':
    main()