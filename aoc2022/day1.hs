import Data.List.Extra
import Functions

main = do
  input <- lines <$> readFile "input/day1.in"
  let nums = map sum (parseGroup input [])
  let ansP1 = maximum nums
  let ansP2 = sum (take 3 (reverse $ sort nums))
  print ansP1
  print ansP2
