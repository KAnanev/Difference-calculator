from gendiff.parser import deserializer, parse_args


def test_deserializer():
    assert isinstance(deserializer('data/before_plain.json'), dict)
    assert isinstance(deserializer('data/before_plain.yaml'), dict)
    assert isinstance(deserializer('data/after_plain.yml'), dict)


def test_parse_args():
    parser = parse_args(['file.json', 'file.json'])
    assert parser.first_file
    assert parser.second_file
    assert parser.format
