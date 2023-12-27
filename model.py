import json

from cell import Cell


class Model():
    id: str
    cellList: list
    size: int
  
    def __init__(self, id, cellList, size):
      self.id = id
      self.cellList = cellList
      self.size = size
      
    def from_dict(json) -> 'Model':
        obj = json.loads(json)
        _id = str(obj[''])
        _cellList = str(obj[''])
        _size = str(obj[''])
        return Model(_id, _cellList, _size)
    
    @staticmethod
    def from_map(map_data):
        model =  Model(map_data['id'], Cell.from_map(map_data['cellList']), map_data['size'])
        return model
