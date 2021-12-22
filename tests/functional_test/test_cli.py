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


def test_cli_diff_plain(answer_data):
    command = ['poetry', 'run', 'gendiff', 'tests/fixtures/file1.json', 'tests/fixtures/file2.json']
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out == answer_data
    assert err == b''