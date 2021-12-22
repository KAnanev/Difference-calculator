import subprocess


def capture(command):
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = proc.communicate()
    return out, err, proc.returncode


def test_cli(error_cli_data):
    command = ['poetry', 'run', 'gendiff']
    out, err, exitcode = capture(command)
    assert exitcode == 2
    assert out == b''
    assert err == error_cli_data


def test_cli_help(cli_data):
    command = ['poetry', 'run', 'gendiff', '-h']
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out == cli_data
    assert err == b''


def test_cli_diff_plain(cli_answer_data):
    command = ['poetry', 'run', 'gendiff', 'tests/fixtures/before_plain.json', 'tests/fixtures/after_plain.json']
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out == cli_answer_data + b'\r\n'
    assert err == b''
