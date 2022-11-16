"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730521912"


class Simpy:
    values: list[float]


    def __init__(self, xs: list[float]):
        self.values = xs

    def __repr__(self):
        return f"Simpy({self.values})"
    
    def fill(self, content: float, times: int):
        for _ in range(times):
            self.values.append(content)
    
    def arange(self, start: float, stop: float, step: float = 1):
        assert step != 0.0
        if step > 0:
            while start < stop:
                self.values.append(start)
                start += step
        else:
            while start > stop:
                self.values.append(start)
                start += step
    
    def sum(self):
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        x = Simpy([])
        if type(rhs) == float:
            for i in range(len(self.values)):
                x.values.append(self.values[i] + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                x.values.append(self.values[i] + rhs.values[i])
        return x

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        x = Simpy([])
        if type(rhs) == float:
            for i in range(len(self.values)):
                x.values.append(self.values[i] ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                x.values.append(self.values[i] ** rhs.values[i])
        return x
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        x = []
        if type(rhs) == float:
            for i in range(len(self.values)):
                x.append(self.values[i] == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                x.append(self.values[i] == rhs.values[i])
        return x

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        x = []
        if type(rhs) == float:
            for i in range(len(self.values)):
                x.append(self.values[i] > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                x.append(self.values[i] > rhs.values[i])
        return x

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        if type(rhs) == int:
            return self.values[rhs]
        else:
            x = Simpy([])
            for i in range(len(rhs)):
                if rhs[i]:
                    x.values.append(self.values[i])
            return x
    

        
    # TODO: Your constructor and methods will go here.