import headerparser

# Taking into account that the dependencies are separated by commas and pipes
# In this case, I assume the OR dependencies(|) are the same as the comma dependencies(,) and are both required
def split_dependencies(dependencies_string): 
    dependencies = []
    for y in dependencies_string.replace(" ","").replace('|',",").split(','):
        dependencies.append(y)
    if len(dependencies) > 1:
        return dependencies
    else:
        return [dependencies_string.replace(" ","")]

parser = headerparser.HeaderParser()
parser.add_field("Package", required=True)
parser.add_field("Architecture", required=True)
parser.add_field("Version", required=True)
parser.add_field("Depends", "Pre-Depends", "Recommends" , default = [], multiple=True, type = lambda x: split_dependencies(x))
parser.add_field("Suggests", "Enhances" ,default=[], multiple=True, type = lambda x: split_dependencies(x))
parser.add_field("Conflicts", "Breaks", "Replaces", default=[], multiple=True, type = lambda x: split_dependencies(x))
parser.add_field("Provides", default=[], type = lambda x: split_dependencies(x))
parser.add_field("Section")
parser.add_field("Size")
parser.add_field("Filename")
parser.add_additional(enable = True)
# parser.add_field("Pre-Depends", default=[])
# parser.add_field("Recommends", default=[])
# parser.add_field("Replaces", default=[])
# parser.add_field("Enhances", default=[])
# parser.add_field("Breaks", default=[])