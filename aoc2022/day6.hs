import Data.List

main = do
  input <- head . lines <$> readFile "input/day6.in"
  let ansP1 = getMarker input 0 4
  let ansP2 = getMarker input 0 14
  putStrLn $ "Part 1: " ++ show ansP1
  putStrLn $ "Part 2: " ++ show ansP2

getMarker :: String -> Int -> Int -> Int
getMarker m c x
  | length (nub $ take x m) == x = c + x
  | otherwise = getMarker (drop 1 m) (c + 1) x
