import Functions

main = do
  input <- map parseList . lines <$> readFile "input/day4.in"
  let ansP1 = getOverlaps input 0 all
      ansP2 = getOverlaps input 0 any
  print ansP1
  print ansP2

getOverlaps :: (Eq a, Num t, Enum a) => [[a]] -> t -> ((a -> Bool) -> [a] -> Bool) -> t
getOverlaps [] n _ = n
getOverlaps (x : xs) n f =
  let l1 = [(head x) .. (x !! 1)]
      l2 = [(x !! 2) .. (last x)]
      hasOverlap = f ((== True) . (`elem` l1)) l2 || f ((== True) . (`elem` l2)) l1
   in getOverlaps xs (if hasOverlap then n + 1 else n) f
