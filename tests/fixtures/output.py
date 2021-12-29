output_error_cli = """usage: gendiff [-h] [-f FORMAT] first_file second_file
gendiff: error: the following arguments are required: first_file, second_file
"""

output_cli_help = """usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output"""

output_plain = """{
 - follow: false
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: true
}"""