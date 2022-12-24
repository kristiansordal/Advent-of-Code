import Data.Bifunctor as Bf
import Data.List
import Data.Map (Map)
import Data.Map qualified as Map
import Data.Map.Strict qualified as Map
import Functions

main = do
  input <- map parseCharToNum . lines <$> readFile "input/day12.in"
  let start = (0, 20)
  let end = (148, 20)
  print ((input !! 20) !! 148)
  print (head (input !! 20))

bfs :: [[Int]] -> [(Int, Int)] -> Map (Int, Int) Int -> (Int, Int) -> (Int, Int) -> Int
bfs m toSearch v c e
  | isNull toSearch = fst e
  | otherwise = 
  where
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    toSearch' = toSearch ++ map (Bf.bimap (fst c +) (snd c +)) dirs
