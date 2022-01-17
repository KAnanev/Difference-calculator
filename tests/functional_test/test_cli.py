import subprocess

from tests.fixtures.output import output_flat, output_cli_help, \
    output_error_cli, output_nested


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
    assert err == output_error_cli.encode()


def test_cli_help():
    command = ['poetry', 'run', 'gendiff', '-h']
    out, err, exitcode = capture(command)
    print(out)
    assert exitcode == 0
    assert out.startswith(output_cli_help)
    assert err == b''


def test_cli_diff_plain():
    command = ['poetry', 'run', 'gendiff',
               'data/before_flat.json', 'data/after_flat.json']
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out.startswith(output_flat.encode())
    assert err == b''


def test_cli_diff_nested():
    command = ['poetry', 'run', 'gendiff',
               'data/before_nested.json', 'data/after_nested.json']
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out.startswith(output_nested.encode())
    assert err == b''
