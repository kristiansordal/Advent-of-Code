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

-- import Data.Set qualified as S (Set, delete, findMax, findMin, foldl, fromList, map, member, notMember, union)

-- -- import Data.S.Set qualified as S (map)

-- parseInput :: String -> S.Set (Int, Int, Int)
-- parseInput = S.fromList . map ((read . ("(" ++)) . (++ ")")) . lines

-- getNeighbours :: S.Set (Int, Int, Int) -> (Int, Int, Int) -> [(Int, Int, Int)]
-- getNeighbours world (x, y, z) = filter (`S.member` world) [(x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)]

-- getSurface :: S.Set (Int, Int, Int) -> Int
-- getSurface world = foldl (flip $ (+) . (6 -) . length . getNeighbours world) 0 world

-- getNegativeSpace :: S.Set (Int, Int, Int) -> S.Set (Int, Int, Int)
-- getNegativeSpace world = S.fromList [(x, y, z) | x <- [minX .. maxX], y <- [minY .. maxY], z <- [minZ .. maxZ], (x, y, z) `S.notMember` world]
--   where
--     xs = S.map (\(x, _, _) -> x) world
--     ys = S.map (\(_, y, _) -> y) world
--     zs = S.map (\(_, _, z) -> z) world
--     (minX, minY, minZ) = (S.findMin xs - 1, S.findMin ys - 1, S.findMin zs - 1)
--     (maxX, maxY, maxZ) = (S.findMax xs + 1, S.findMax ys + 1, S.findMax zs + 1)

-- getInside :: S.Set (Int, Int, Int) -> [(Int, Int, Int)] -> S.Set (Int, Int, Int)
-- getInside negative [] = negative
-- getInside negative (el : queue) = getInside negative' queue'
--   where
--     neighbours = getNeighbours negative el
--     negative' = foldl (flip S.delete) negative neighbours
--     queue' = queue ++ neighbours

-- main = do
--   input <- parseInput <$> readFile "input/day18.in"
--   let negative = getNegativeSpace input
--   let start = S.findMin negative
--   let inside = getInside (S.delete start negative) [start]
--   let lavaDrop = input `S.union` inside
--   print $ getSurface input
--   print $ getSurface lavaDrop
