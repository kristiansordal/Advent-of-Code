import Data.Set (Set)
import Data.Set qualified as Set

main = do
  input <- head . lines <$> readFile "input/day6.in"
  let ansP1 = getMarker input 0 4
  let ansP2 = getMarker input 0 14
  print ansP1
  print ansP2

getMarker :: String -> Int -> Int -> Int
getMarker m c x =
  let s = Set.fromList (take x m)
   in if length s == x
        then c + x
        else getMarker (drop 1 m) (c + 1) x
