import Data.List.Extra
import Data.Set (Set)
import Data.Set qualified as Set
import Functions

main = do
  input <- map (map parseTupParen . splitOn "->") . lines <$> readFile "input/day14.in"
  let set = Set.fromList (concat $ world input [])
      abyss = maximum $ map snd (concat input)
      ansP1 = sand set (500, 0) abyss 0
      ansP2 = sand' set (500, 0) abyss 0
  print ansP1
  print ansP2

sand :: Set (Integer, Integer) -> (Integer, Integer) -> Integer -> Integer -> Integer
sand coords pos a c
  | Set.member next coords =
      if Set.member left coords
        then
          if Set.member right coords
            then sand (Set.insert pos coords) (500, 0) a (c + 1)
            else sand coords right a c
        else sand coords left a c
  | snd next > a = c
  | otherwise = sand coords next a c
  where
    next = (fst pos, snd pos + 1)
    right = (fst pos + 1, snd pos + 1)
    left = (fst pos - 1, snd pos + 1)

sand' :: Set (Integer, Integer) -> (Integer, Integer) -> Integer -> Integer -> Integer
sand' coords pos a c
  | Set.member (500, 0) coords = c
  | Set.member next coords =
      if Set.member left coords
        then
          if Set.member right coords
            then sand' (Set.insert pos coords) (500, 0) a (c + 1)
            else sand' coords right a c
        else sand' coords left a c
  | snd next == a + 2 = sand' (Set.insert pos coords) (500, 0) a (c + 1)
  | otherwise = sand' coords next a c
  where
    next = (fst pos, snd pos + 1)
    right = (fst pos + 1, snd pos + 1)
    left = (fst pos - 1, snd pos + 1)

world :: [[(Integer, Integer)]] -> [[(Integer, Integer)]] -> [[(Integer, Integer)]]
world [] s = s
world ([] : xs) s = world xs s
world ([x] : xs) s = world xs (s ++ [[x]])
world ((x : y : xs) : xss) s = world ((y : xs) : xss) (s ++ [seg x y])

seg :: (Integer, Integer) -> (Integer, Integer) -> [(Integer, Integer)]
seg (x1, y1) (x2, y2)
  | x1 == x2 && y1 <= y2 = [(x1, y) | y <- [y1 .. y2]]
  | x1 == x2 && y1 >= y2 = [(x1, y) | y <- [y2 .. y1]]
  | y1 == y2 && x1 <= x2 = [(x, y1) | x <- [x1 .. x2]]
  | y1 == y2 && x1 >= x2 = [(x, y1) | x <- [x2 .. x1]]
