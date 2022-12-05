import Functions

main = do
  input <- map parseNums . lines <$> readFile "input/day4.in"
  let ansP1 = getOverlaps input 0 all
      ansP2 = getOverlaps input 0 any
  print ansP1
  print ansP2

getOverlaps :: (Eq a, Num t, Enum a) => [[a]] -> t -> ((a -> Bool) -> [a] -> Bool) -> t
getOverlaps [] n f = n
getOverlaps (x : xs) n f =
  let l1 = [(head x) .. (x !! 1)]
      l2 = [(x !! 2) .. (last x)]
   in if f ((== True) . (`elem` l1)) l2 || f ((== True) . (`elem` l2)) l1
        then getOverlaps xs (n + 1) f
        else getOverlaps xs n f
