import subprocess


def capture(command):
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = proc.communicate()
    return out, err, proc.returncode


def test_cli_flat():
    command = ['poetry', 'run', 'gendiff', '-h']
    out, err, exitcode = capture(command)
    assert exitcode == 0


def test_cli_diff_flat():
    command = ['poetry', 'run', 'gendiff',
               'data/before_flat.json', 'data/after_flat.json']
    out, err, exitcode = capture(command)
    assert exitcode == 0


def test_cli_diff_nested():
    command = ['poetry', 'run', 'gendiff',
               'data/before_nested.json', 'data/after_nested.json']
    out, err, exitcode = capture(command)
    assert exitcode == 0


def test_cli_diff_plain():
    command = ['poetry', 'run', 'gendiff', '-f', 'plain',
               'data/before_flat.json', 'data/after_flat.json']
    out, err, exitcode = capture(command)
    assert exitcode == 0
