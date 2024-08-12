'''
Завдання 3:
Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію пошуку по group/number і повернення значення timingExbytes/incoming
результат виведіть у консоль через логер на рівні інфо
'''
import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def find_incoming_value(group_number):
    xml_file = 'groups.xml'
    # Парсим XML файл
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Поиск элемента group с заданным number
    for group in root.findall('group'):
        number = group.find('number')
        if number is not None and number.text == group_number:
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')
                if incoming is not None:
                    logging.info(f"Incoming value for group/number {group_number}: {incoming.text}")
                    return incoming.text
            break
    logging.info(f"No incoming value found for group/number {group_number}")
    return None


find_incoming_value('2')