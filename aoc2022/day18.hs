import Data.Set (Set)
import Data.Set qualified as Set
import Functions

main = do
  input <- map parseList . lines <$> readFile "input/day18.in"
  print (checkCubes input)

checkCubes :: [[Integer]] -> Int
checkCubes cubes = length cubes * 6 - foldr ((+) . checkOne cubes) 0 cubes

checkOne :: [[Integer]] -> [Integer] -> Int
checkOne cubes cube = fromIntegral $ length sums
  where
    dirs = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    sums = filter (`elem` dirs) (map (map abs . zipWith (-) cube) cubes)
