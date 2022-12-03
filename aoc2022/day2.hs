import Data.Bifunctor

main = do
  input <- map parse . lines <$> readFile "input/day2.in"
  let nums = map (Data.Bifunctor.bimap parseNum parseNum) input
  print nums
  let ansP1 = rps nums
  let ansP2 = rps' input 0
  print ansP1
  print ansP2

rps :: [(Integer, Integer)] -> Integer
rps = sum . map (\x -> (snd x - fst x + 1) `mod` 3 * 3 + snd x)

rps' :: [(Char, Char)] -> Integer -> Integer
rps' [] sc = sc
rps' (x : xs) sc
  | x == ('A', 'X') = rps' xs (sc + 3)
  | x == ('A', 'Y') = rps' xs (sc + 4)
  | x == ('A', 'Z') = rps' xs (sc + 8)
  | x == ('B', 'X') = rps' xs (sc + 1)
  | x == ('B', 'Y') = rps' xs (sc + 5)
  | x == ('B', 'Z') = rps' xs (sc + 9)
  | x == ('C', 'X') = rps' xs (sc + 2)
  | x == ('C', 'Y') = rps' xs (sc + 6)
  | x == ('C', 'Z') = rps' xs (sc + 7)

parse :: String -> (Char, Char)
parse s = (head s, last s)

parseNum :: Char -> Integer
parseNum s
  | s == 'A' || s == 'X' = 1
  | s == 'B' || s == 'Y' = 2
  | s == 'C' || s == 'Z' = 3
