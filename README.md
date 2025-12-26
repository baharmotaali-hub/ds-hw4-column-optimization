# ds-hw4-column-optimization
Approach Summary

Each block’s dimensions are first sorted so that x ≥ y ≥ z, allowing consistent handling of rotations where (x, y) form the base and z is the height.

The solution considers two cases:

1 Single block:
The stability is simply the smallest dimension (z). The best single block is tracked.

2 Two stacked blocks:
Blocks are grouped by their base dimensions (x, y) using a hash table.
For each group, the two blocks with the largest heights are selected.
The stability of stacking them is calculated as min(y, z₁ + z₂).

Using a hash table avoids unnecessary pairwise comparisons and ensures an overall time complexity of O(N).