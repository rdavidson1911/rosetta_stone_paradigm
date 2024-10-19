from parsers import get_parser

def parse_packet_file(file_path, file_format):
    parser = get_parser(file_format)
    if parser:
        return parser.parse(file_path)
    else:
        return f"No parser available for format: {file_format}"

def main():
    formats = ['json', 'xml', 'txt', 'psml', 'pcapng']
    for format in formats:
        file_path = f"path/to/your/{format}_file.{format}"
        result = parse_packet_file(file_path, format)
        print(f"Parsed {format.upper()} file:")
        print(result)
        print("---")

if __name__ == "__main__":
    main()
