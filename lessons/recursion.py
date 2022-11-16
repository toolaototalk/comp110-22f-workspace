from __future__ import annotations

from typing import Union
   
class Node:
    data: int
    next: Union[Node, None]

    def __init__(self, data: int, next: Union[Node, None]):
        self.data = data
        self.next = next