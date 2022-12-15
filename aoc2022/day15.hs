import Data.Set (Set)
import Data.Set qualified as Set
import Functions

main = do
  input <- map (parseBeacon . parseList) . lines <$> readFile "input/day15.in"
  let ansP1 = oneRow input 2000000 Set.empty
  print ansP1

oneRow :: [[(Integer, Integer)]] -> Integer -> Set Integer -> Integer
oneRow [] line set = fromIntegral $ length (Set.toList set)
oneRow (x : xs) line set
  | yDist <= man = oneRow xs line (Set.union set (Set.fromList [(sx - (man - yDist)) .. (sx + (man - yDist - 1))]))
  | otherwise = oneRow xs line set
  where
    sx = fst $ head x
    sy = snd $ head x
    bx = fst $ last x
    by = snd $ last x
    man = manhattan (head x) (last x)
    yDist = abs (line - sy)

updateSet :: Integer -> Integer -> Set Integer -> Set Integer
updateSet s e set
  | s < e = updateSet (s + 1) e (Set.insert s set)
  | otherwise = set

parseBeacon :: [Integer] -> [(Integer, Integer)]
parseBeacon (x : y : z : w : ws) = [(x, y), (z, w)]
