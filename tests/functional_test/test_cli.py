import subprocess


def capture(command):
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = proc.communicate()
    return out, err, proc.returncode


def test_cli():
    command = ['poetry', 'run', 'gendiff']
    out, err, exitcode = capture(command)
    assert exitcode == 2
    assert out == b''
    assert err == b'usage: gendiff [-h] [-f FORMAT] first_file second_file\r\ngendiff: ' \
                  b'error: the following arguments are required: first_file, second_file\r\n'


def test_cli_help():
    command = ['poetry', 'run', 'gendiff', '-h']
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out == b'usage: gendiff [-h] [-f FORMAT]' \
                  b' first_file second_file\r\n\r\n' \
                  b'Generate diff\r\n\r\npositional' \
                  b' arguments:\r\n  first_file            ' \
                  b'First argument\r\n  second_file           ' \
                  b'Second argument\r\n\r\noptional arguments:\r\n  -h, --help            ' \
                  b'show this help message and exit\r\n  -f FORMAT, --format FORMAT\r\n                        ' \
                  b'set format of output.\r\n'
    assert err == b''
