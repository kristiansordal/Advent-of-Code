import Data.List
import Data.Set (Set)
import Data.Set qualified as Set

main = do
  input <- head . lines <$> readFile "input/day17.in"
  let ansP1 = moves input (Set.fromList [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]) 0 3 0
  let ansP2 = findCycle input (Set.fromList [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]) [] 0 3 0
  print ansP1
  print ansP2

-- moves input (Set.fromList [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]) 0 3 0

type Tetromino = [(Integer, Integer)]

findCycle :: String -> Set (Integer, Integer) -> [Set (Integer, Integer)] -> Integer -> Integer -> Int -> Set (Integer, Integer)
findCycle s set setList t h index
  | t `mod` 100 == 0 =
      case cyc setList 0 of
        Nothing -> findCycle s set' (setList ++ [set']) (t + 1) h' index'
        (Just cyc) -> cyc
  | otherwise = findCycle s set' (setList ++ [set']) (t + 1) h' index'
  where
    h' = if not (Set.null set) then maximum (map snd (Set.toList set)) else 0
    (set', index') = move s index set tet
    tet = tetromino (t `mod` 5) h'

cyc :: [Set (Integer, Integer)] -> Int -> Maybe (Set (Integer, Integer))
cyc s i
  | i > length s = Nothing
  | curr `elem` s' = Just curr
  | otherwise = cyc s (i + 1)
  where
    curr = s !! i
    s' = drop (i + 1) s

moves :: String -> Set (Integer, Integer) -> Integer -> Integer -> Int -> Integer
moves s set t h index
  | t == 2022 = h'
  | otherwise = moves s set' (t + 1) h' index'
  where
    h' = if not (Set.null set) then maximum (map snd (Set.toList set)) else 0
    (set', index') = move s index set tet
    tet = tetromino (t `mod` 5) h'

move :: String -> Int -> Set (Integer, Integer) -> Tetromino -> (Set (Integer, Integer), Int)
move m time s t =
  case vertical t' s of
    (Left s') -> (s', time + 1)
    (Right t'') ->
      move m (time + 1) s t''
  where
    x = m !! (time `mod` length m)
    t' = horizontal x s t

tetromino :: Integer -> Integer -> Tetromino
tetromino s h
  | s == 0 = [(2, h + 4), (3, h + 4), (4, h + 4), (5, h + 4)]
  | s == 1 = [(3, h + 6), (2, h + 5), (3, h + 5), (4, h + 5), (3, h + 4)]
  | s == 2 = [(4, h + 6), (4, h + 5), (2, h + 4), (3, h + 4), (4, h + 4)]
  | s == 3 = [(2, h + 7), (2, h + 6), (2, h + 5), (2, h + 4)]
  | s == 4 = [(2, h + 5), (3, h + 5), (2, h + 4), (3, h + 4)]

horizontal :: Char -> Set (Integer, Integer) -> Tetromino -> Tetromino
horizontal c s t
  | c == '>' =
      let m = map (\(x, y) -> (x + 1, y)) t
       in if any ((> 6) . fst) m || any (`Set.member` s) m then t else m
  | c == '<' =
      let m = map (\(x, y) -> (x - 1, y)) t
       in if any ((< 0) . fst) m || any (`Set.member` s) m then t else m

vertical :: Tetromino -> Set (Integer, Integer) -> Either (Set (Integer, Integer)) Tetromino
vertical t s
  | any (`Set.member` s) t' = Left (Set.union s (Set.fromList t))
  | otherwise = Right t'
  where
    t' = map (\(x, y) -> (x, y - 1)) t

p :: Set (Integer, Integer) -> Set (Integer, Integer) -> (Integer, Integer) -> String -> [String] -> [String]
p s s' m str strL
  | snd m == -1 = strL
  | Set.member m s = p s (Set.insert m s') (fst m + 1, snd m) (str ++ "█") strL
  | fst m > 6 = p s s' (0, snd m - 1) "" (strL ++ [str])
  | otherwise = p s s' (fst m + 1, snd m) (str ++ ".") strL
