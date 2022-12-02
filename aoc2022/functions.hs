module Functions where

import Data.List.Extra
import Data.Map (Map)
import Data.Map qualified as Map
import Data.Set (Set)
import Data.Set qualified as Set
import Text.Regex

parseNum :: String -> Integer
parseNum = read

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
