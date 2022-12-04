import Data.List.Extra
import Functions

main = do
  input <- map (fst . line1) . lines <$> readFile "input/day1.in"
  let nums = map sum (parseGroup input [])
  let ansP1 = getMostCals nums
  let ansP2 = getThreeMostCals nums
  print ansP1
  print ansP2

getMostCals :: [Integer] -> Integer
getMostCals = maximum

getThreeMostCals :: [Integer] -> Integer
getThreeMostCals l = sum (take 3 (reverse $ sort l))
