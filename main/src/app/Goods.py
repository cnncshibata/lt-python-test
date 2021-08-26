from dataclasses import dataclass, field


@dataclass
class Good:
    id: int
    name: str
    stock: int

    
@dataclass
class Goods:
    goods: dict[int, Good] = field(default_factory=dict)

    def add(self, good: Good):
        self.goods[good.id] = good

    def get_by_id(self, id: int) -> Good:
        try:
            return self.goods[id]
        except:
            raise Exception
    
    def remove_by_id(self, id: int):
        self.goods.pop(id)

    def clear(self):
        self.goods.clear()
    
    def len(self):
        return len(self.goods)
