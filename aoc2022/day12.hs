import Data.List
import Data.Map.Strict qualified as Map
import Functions

main = do
  input <- map parseCharToNum . lines <$> readFile "input/day12.in"
  print "asdf"

bfs :: [[Int]] -> (Int, Int) -> (Int, Int) -> Int

bfs
