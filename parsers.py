import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

class PacketParser(ABC):
    @abstractmethod
    def parse(self, file_path):
        pass

class JSONParser(PacketParser):
    def parse(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

class XMLParser(PacketParser):
    def parse(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        return self._element_to_dict(root)

    def _element_to_dict(self, element):
        result = {}
        for child in element:
            if len(child) == 0:
                result[child.tag] = child.text
            else:
                result[child.tag] = self._element_to_dict(child)
        return result

class PlainTextParser(PacketParser):
    def parse(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return self._parse_lines(lines)

    def _parse_lines(self, lines):
        result = {}
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                result[key.strip()] = value.strip()
        return result

class PSMLParser(PacketParser):
    def parse(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        packets = []
        for packet in root.findall('.//packet'):
            packet_data = {}
            for section in packet.findall('section'):
                packet_data[section.get('name')] = section.text
            packets.append(packet_data)
        return packets

class PCAPNGParser(PacketParser):
    def parse(self, file_path):
        # This is a placeholder. Parsing pcapng files requires a specialized library.
        print(f"Parsing pcapng file: {file_path}")
        print("Note: Actual pcapng parsing not implemented. Consider using a library like 'scapy' for this.")
        return {"warning": "pcapng parsing not implemented"}

def get_parser(file_format):
    parsers = {
        'json': JSONParser(),
        'xml': XMLParser(),
        'txt': PlainTextParser(),
        'psml': PSMLParser(),
        'pcapng': PCAPNGParser()
    }
    return parsers.get(file_format.lower())
