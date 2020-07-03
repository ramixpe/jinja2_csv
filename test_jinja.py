import csv
from jinja2 import Template
source_file = 'book2.csv'
interface_template_file = 'template.j2'

with open(interface_template_file) as f:
    interface_template = Template(f.read(),keep_trailing_newline=True)

interafce_configs = ""
with open(source_file) as f:
    reader = csv.DictReader(f)
    for raw in reader:
        interface_config = interface_template.render(
            interface = raw['interface'],
            description = raw['description'],
            address = raw['address']
        )
        interafce_configs += interface_config
print(interafce_configs)
