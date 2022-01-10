output_error_cli = """usage: gendiff [-h] [-f FORMAT] first_file second_file
gendiff: error: the following arguments are required: first_file, second_file
"""

output_cli_help = b'usage: gendiff [-h] [-f FORMAT] first_file second_file\n\nGenerate diff\n\npositional arguments:\n  first_file\n  second_file\n\noptions:\n  -h, --help            show this help message and exit\n  -f FORMAT, --format FORMAT\n                        set formatter of output\n'

output_plain = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

output_nested = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
