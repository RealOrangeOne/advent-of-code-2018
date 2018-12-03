from collections import namedtuple, Counter
import re

CLAIM_RE = re.compile("#(\d+?) @ (\d+?),(\d+?): (\d+?)x(\d+)")

_Claim = namedtuple('Claim', ['id', 'start_x', 'start_y', 'width', 'height'])

class Claim(_Claim):
    def internal_coordinates(self):
        coordinates = []
        for x in range(self.start_x, self.start_x + self.width):
            for y in range(self.start_y, self.start_y + self.height):
                coordinates.append((x, y))
        return coordinates


with open('data.txt', 'r') as f:
    claims = [
        Claim(*[int(num) for num in CLAIM_RE.match(line).groups()])
        for line in f.readlines()
    ]

claim_patches = []

for claim in claims:
    claim_patches.extend(claim.internal_coordinates())

claim_patch_counter = Counter(claim_patches)

claim_patch_counter_values = list(claim_patch_counter.values()).count(1)

conflicting_patches = {patch for patch, count in claim_patch_counter.items() if count > 1}

print(len(conflicting_patches))

for claim in claims:
    for claim_patch in claim.internal_coordinates():
        if claim_patch in conflicting_patches:
            break
    else:
        print(claim.id)
