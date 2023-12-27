class Cell():
    urlImage : str
    name : str

    def __init__(self, urlImage,name):
        self.urlImage = urlImage
        self.name = name

    def from_json(json):
        data = json.loads(json)
        return Cell(data['urlImage'], data['name'])
    @staticmethod
    def from_map(map_data):
        cells = []
        for cell in map_data:             
            cells.append(Cell(cell['urlImage'], cell['name']))
        return cells