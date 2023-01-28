import Data.List.Extra
import Data.Set (Set)
import Data.Set qualified as Set
import Functions

main = do
  input <- map (map parseTupParen . splitOn "->") . lines <$> readFile "input/day14.in"
  let set = Set.fromList (concat $ world input [])
      abyss = maximum $ map snd (concat input)
      ansP1 = sand set (500, 0) abyss 0 False
      ansP2 = sand set (500, 0) abyss 0 True
  print ansP1
  print ansP2

sand :: Set (Integer, Integer) -> (Integer, Integer) -> Integer -> Integer -> Bool -> Integer
sand coords pos a c p
  | Set.member (500, 0) coords && p = c
  | Set.member next coords =
      if Set.member left coords
        then
          if Set.member right coords
            then sand (Set.insert pos coords) (500, 0) a (c + 1) p
            else sand coords right a c p
        else sand coords left a c p
  | snd next > a && not p = c
  | snd next == a + 2 && p = sand (Set.insert pos coords) (500, 0) a (c + 1) p
  | otherwise = sand coords next a c p
  where
    next = (fst pos, snd pos + 1)
    right = (fst pos + 1, snd pos + 1)
    left = (fst pos - 1, snd pos + 1)

world :: [[(Integer, Integer)]] -> [[(Integer, Integer)]] -> [[(Integer, Integer)]]
world [] s = s
world ([] : xs) s = world xs s
world ([x] : xs) s = world xs (s ++ [[x]])
world ((x : y : xs) : xss) s = world ((y : xs) : xss) (s ++ [seg x y])
