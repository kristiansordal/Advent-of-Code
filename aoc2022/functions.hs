module Functions where

import Data.List.Extra
import Data.Map (Map)
import Data.Map qualified as Map
import Data.Set (Set)
import Data.Set qualified as Set
import Text.Regex

parseGroup :: [String] -> [Integer] -> [[Integer]]
parseGroup [] ys = [ys]
parseGroup (x : xs) ys
  | x == "" = ys : parseGroup xs []
  | otherwise =
      let num = read x
       in parseGroup xs ((:) num ys)

parseNum :: String -> Integer
parseNum = read

parseInt :: String -> Int
parseInt = read

parseCharToNum :: String -> [Int]
parseCharToNum [] = []
parseCharToNum (x : xs)
  | x == 'S' = 0 : parseCharToNum xs
  | x == 'E' = 26 : parseCharToNum xs
  | otherwise = case elemIndex x a of
      (Just c) -> c : parseCharToNum xs
      Nothing -> parseCharToNum xs
  where
    a = "abcdefghijklmnopqrstuvwxyz"

parseTup :: String -> (Integer, Integer)
parseTup s =
  let tup = map read $ splitOn "," s
   in (head tup, last tup)

parseTupParen :: String -> (Integer, Integer)
parseTupParen s =
  let nums = map read $ filter (/= "") $ splitRegex (mkRegex "[^0-9]") s
   in (head nums, last nums)

parseList :: String -> [Integer]
parseList = map read . filter (/= "") . splitRegex (mkRegex "[^0-9]")

parseNumWord :: String -> (String, Integer)
parseNumWord s =
  let word = splitRegex (mkRegex "[^A-z]") s
      num = map read $ filter (/= "") $ splitRegex (mkRegex "[^0-9]") s
   in (head word, head num)

parseNumsWord :: String -> ([String], [Integer])
parseNumsWord s =
  let word = filter (/= "") $ splitRegex (mkRegex "[^A-z*+]") s
      num = map read $ filter (/= "") $ splitRegex (mkRegex "[^0-9]") s
   in (word, num)

parseCharNum :: String -> (Char, Integer)
parseCharNum s = (head $ head $ words s, read $ last $ words s)

parseUDLR :: Char -> (Integer, Integer)
parseUDLR c
  | c == 'U' = (0, 1)
  | c == 'D' = (0, -1)
  | c == 'L' = (-1, 0)
  | c == 'R' = (1, 0)

parseMaybe :: String -> (String, Maybe Int)
parseMaybe s
  | length spl == 1 = (s, Nothing)
  | otherwise = (head spl, Just $ read $ last spl)
  where
    spl = splitOn " " s

parseStrSet :: String -> (Set Char, Set Char)
parseStrSet s =
  let l = length s `div` 2
      f = Set.fromList $ take l s
      h = Set.fromList $ drop l s
   in (f, h)

parseDig :: String -> [Integer]
parseDig = map (\x -> read [x])

type Graph n = Map n (Set n)

-- create a graph
createGraph :: (Ord n) => [[n]] -> Graph n -> Graph n
createGraph xs g = foldl (\g x -> insertMany g (head x) (tail x)) g xs

-- insert many neigbours into the graph
insertMany :: (Ord n) => Graph n -> n -> [n] -> Graph n
insertMany g n = foldr (edgeBetween n) g

-- insert undirected edge
edgeBetween :: (Ord n) => n -> n -> Graph n -> Graph n
edgeBetween n1 n2 = Map.insertWith Set.union n2 (Set.singleton n1) . Map.insertWith Set.union n1 (Set.singleton n2)

remove :: (Eq a) => [a] -> a -> Bool -> [a]
remove [] n _ = []
remove (x : xs) n b
  | n == x && not b = remove xs n True
  | not b = x : remove xs n False
  | otherwise = x : remove xs n True

update :: [a] -> a -> Int -> [a]
update l n x = nl
  where
    (f, s) = splitAt (fromIntegral x) l
    nl = f ++ [n] ++ tail s

insert :: [a] -> a -> Int -> [a]
insert l n x = nl
  where
    (f, s) = splitAt (fromIntegral x) l
    nl = f ++ [n] ++ s

manhattan :: (Integer, Integer) -> (Integer, Integer) -> Integer
manhattan (x1, y1) (x2, y2) = abs (x1 - x2) + abs (y1 - y2)

seg :: (Integer, Integer) -> (Integer, Integer) -> [(Integer, Integer)]
seg (x1, y1) (x2, y2)
  | x1 == x2 && y1 <= y2 = [(x1, y) | y <- [y1 .. y2]]
  | x1 == x2 && y1 >= y2 = [(x1, y) | y <- [y2 .. y1]]
  | y1 == y2 && x1 <= x2 = [(x, y1) | x <- [x1 .. x2]]
  | y1 == y2 && x1 >= x2 = [(x, y1) | x <- [x2 .. x1]]
