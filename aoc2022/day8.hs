import Data.List
import Functions

main = do
  input <- map parseDig . lines <$> readFile "input/day8.in"
  let ansP1 = visibleTrees input (transpose input) (1, 1) (input !! 1 !! 1) ((fromIntegral (length input) * 2) + (fromIntegral (length (head input)) - 2) * 2)
      ansP2 = scenic input (transpose input) (1, 1) (input !! 1 !! 1) []
  putStrLn $ "Part 1: " ++ show ansP1
  putStrLn $ "Part 2: " ++ show ansP2

visibleTrees :: [[Integer]] -> [[Integer]] -> (Int, Int) -> Integer -> Integer -> Integer
visibleTrees t t' pos x c
  | pos == (fromIntegral $ length t - 2, fromIntegral $ length t - 2) = c + isVisible' x dirs
  | snd pos == fromIntegral (length t) - 2 = visibleTrees t t' (fst pos + 1, 1) (t !! (fst pos + 1) !! 1) (c + vis)
  | otherwise = visibleTrees t t' (fst pos, snd pos + 1) (t !! fst pos !! (snd pos + 1)) (c + vis)
  where
    row = splitAt (fromIntegral (snd pos)) (t !! fst pos)
    col = splitAt (fromIntegral (fst pos)) (t' !! snd pos)
    dirs = [reverse $ fst row, tail $ snd row, reverse $ fst col, tail $ snd col]
    vis = isVisible' x dirs

scenic :: [[Integer]] -> [[Integer]] -> (Int, Int) -> Integer -> [Integer] -> Integer
scenic t t' pos x c
  | pos == (fromIntegral $ length t - 2, fromIntegral $ length t - 2) = maximum c
  | snd pos == fromIntegral (length t) - 2 = scenic t t' (fst pos + 1, 1) (t !! (fst pos + 1) !! 1) (vis : c)
  | otherwise = scenic t t' (fst pos, snd pos + 1) (t !! fst pos !! (snd pos + 1)) (vis : c)
  where
    row = splitAt (fromIntegral (snd pos)) (t !! fst pos)
    col = splitAt (fromIntegral (fst pos)) (t' !! snd pos)
    dirs = [reverse $ fst row, tail $ snd row, reverse $ fst col, tail $ snd col]
    vis = product $ map (snd . isVisible x) dirs

isVisible :: Integer -> [Integer] -> (Bool, Integer)
isVisible x t
  | length t /= l = (length t == l, fromIntegral l + 1)
  | otherwise = (length t == l, fromIntegral l)
  where
    l = length (takeWhile (< x) t)

isVisible' :: Integer -> [[Integer]] -> Integer
isVisible' x dirs
  | any (((== True) . fst) . isVisible x) dirs = 1
  | otherwise = 0
