import Data.Bifunctor

main = do
  input <- map parse . lines <$> readFile "day2.in"
  let nums = map (Data.Bifunctor.bimap parseNum parseNum) input
  let ansP1 = rps nums
  let ansP2 = rps' input 0
  let ansP2' = rps'' nums
  print ansP1
  print ansP2
  print ansP2'

-- A X = ROCK
-- B Y = PAPER
-- C Z = Sciszz
-- rock scor : 1, 4 ,7
-- pap  scor : 2, 5 ,8
-- scis scor : 3, 6 ,9
--
rps :: [(Integer, Integer)] -> Integer
rps l = sum $ map (\x -> (snd x - fst x + 1) `mod` 3 * 3 + snd x) l

rps'' :: [(Integer, Integer)] -> Integer
rps'' l = sum $ map (\x -> (snd x + fst x - 1) `mod` 3 * (3 + snd x)) l

-- j * 3 + (i + j + 2) % 3 + 1
-- (ord(i[1]) + ord(i[0]) - 1) % 3 + 1 + (ord(i[1]) - 88) * 3

rps' :: [(Char, Char)] -> Integer -> Integer
rps' [] sc = sc
rps' (x : xs) sc
  -- r lose
  | x == ('A', 'X') = rps' xs (sc + 3)
  -- r draw
  | x == ('A', 'Y') = rps' xs (sc + 4)
  -- r win
  | x == ('A', 'Z') = rps' xs (sc + 8)
  -- p l
  | x == ('B', 'X') = rps' xs (sc + 1)
  -- p d
  | x == ('B', 'Y') = rps' xs (sc + 5)
  -- p w
  | x == ('B', 'Z') = rps' xs (sc + 9)
  -- s l
  | x == ('C', 'X') = rps' xs (sc + 2)
  -- s d
  | x == ('C', 'Y') = rps' xs (sc + 6)
  -- s w
  | x == ('C', 'Z') = rps' xs (sc + 7)

parse :: String -> (Char, Char)
parse s = (head s, last s)

parseNum :: Char -> Integer
parseNum s
  | s == 'A' || s == 'X' = 1
  | s == 'B' || s == 'Y' = 2
  | s == 'C' || s == 'Z' = 3
