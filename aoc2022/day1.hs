import Data.List.Extra

main = do
  input <- map parse . lines <$> readFile "input/day1.in"
  let nums = map sum (parse' input [])
  let ansP1 = getMostCals nums
  let ansP2 = getThreeMostCals nums
  print nums
  print ansP1
  print ansP2

getMostCals :: [Integer] -> Integer
getMostCals = maximum

getThreeMostCals :: [Integer] -> Integer
getThreeMostCals l = sum (take 3 (reverse $ sort l))

parse' :: [String] -> [Integer] -> [[Integer]]
parse' [] ys = [ys]
parse' (x : xs) ys
  | x == "" = ys : parse' xs []
  | otherwise =
      let num = read x
       in parse' xs ((:) num ys)

parse :: String -> String
parse s =
  let st = line1 s
   in fst st
