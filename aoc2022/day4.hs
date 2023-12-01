import Functions

main = do
  input <- map parseList . lines <$> readFile "input/day4.in"
  let ansP1 = length . filter id $ map (\[x, y, z, w] -> x <= z && y >= w || x >= z && y <= w) input
      ansP2 = length . filter id $ map (\[x, y, z, w] -> y >= z && w >= x) input
  print ansP1
  print ansP2
