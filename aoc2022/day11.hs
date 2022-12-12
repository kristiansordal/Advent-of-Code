{-# OPTIONS_GHC -Wno-missing-fields #-}

import Data.List.Extra
import Functions

main = do
  input <- splitOn "\n\n" <$> readFile "input/day11.in"
  let monke = map (splitOn "\n") input
      turns = manyTurns 10000 (parseMonkies monke)
      insps = product . take 2 . reverse . sort $ map inspections turns
  print insps

data Monkey = Monkey
  { num :: Integer,
    items :: [Integer],
    op :: ([String], Integer),
    test :: Integer,
    result :: (Integer, Integer),
    inspections :: Integer
  }
  deriving (Show)

manyTurns :: Int -> [Monkey] -> [Monkey]
manyTurns 0 m = m
manyTurns n m = manyTurns (n - 1) (turn m (head m) 0)

turn :: [Monkey] -> Monkey -> Int -> [Monkey]
turn ms fromMonkey t
  | t >= length ms = ms
  | null (items fromMonkey) = turn ms (ms !! (fromIntegral (num fromMonkey) + 1)) (t + 1)
  | otherwise =
      let item = head $ items fromMonkey
          divisor = product $ map test ms
          -- testVal = operation (op fromMonkey) item `div` 3
          testVal = operation (op fromMonkey) item `mod` divisor
          testResult = (testVal `mod` test fromMonkey) == 0
          throw = if testResult then fst (result fromMonkey) else snd (result fromMonkey)
          toMonkey = ms !! fromIntegral throw
          newMonkey = toMonkey {inspections = inspections toMonkey, items = items toMonkey ++ [testVal]}
          oldMonkey = fromMonkey {inspections = inspections fromMonkey + 1, items = remove (items fromMonkey) item False}
          ms' = update ms newMonkey throw
          ms'' = update ms' oldMonkey (num oldMonkey)
       in turn ms'' (ms'' !! fromIntegral (num oldMonkey)) t

operation :: ([String], Integer) -> Integer -> Integer
operation op n
  | snd op == 0 = n * n
  | fst op !! 1 == "+" = snd op + n
  | fst op !! 1 == "*" = snd op * n

parseMonkies :: [[String]] -> [Monkey]
parseMonkies = map (parseMonke Monkey {inspections = 0})

parseMonke :: Monkey -> [String] -> Monkey
parseMonke m [] = m
parseMonke m (x : xs)
  | head s' == "Monkey" = parseMonke (m {num = read $ last s'}) xs
  | head s' == "Starting" =
      let items = parseList s''
       in parseMonke (m {items = items}) xs
  | head s' == "Operation:" =
      let op = drop (length s' - 3) s'
          ops = (take 2 op, read $ last op :: Integer)
       in parseMonke (m {op = ops}) xs
  | head s' == "Test:" = parseMonke (m {test = read $ last s'}) xs
  | head s' == "If" = parseMonke (m {result = (read $ last s' :: Integer, read $ last (splitOn " " (head xs)) :: Integer)}) []
  | otherwise = parseMonke m []
  where
    s' = splitOn " " x
    s'' = concat $ tail $ dropWhile (/= "items:") s'
