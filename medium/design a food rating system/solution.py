from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_heaps = defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            heappush(self.cuisine_heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heappush(self.cuisine_heaps[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        while heap:
            neg_r, f = heap[0]
            if self.food_to_rating[f] == -neg_r:
                return f
            heappop(heap)
        return ""
