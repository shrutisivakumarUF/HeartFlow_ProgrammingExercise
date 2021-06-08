# HeartFlow_ProgrammingExercise

Given Data: .txt file with coordinates of 2D line segments (x1 y1 x2 y2)

Assumptions:

- Two intersecting line segments form a group
- Two non-intersecting line segments with a third intersecting line segment form a group
- A line with no other intersecting line segment(s) forms its own group

Modules

- Shapely: LineString (converts coordinate pairs into line segment objects)
- UnionFind: Self-defined class to implement Union-Find Algorithm

Data Pre-processing/ Sanitization

- Filter out empty list elements
- Rearrange each line internally (left-most x coordinate to the “left”)
- Sort entire list of line segments by x-coordinates

Approach
- Check for pair-wise intersection
- Create groups using the Union-Find Algorithm
- Final count of disjoint sets = Number of groups of line segments



