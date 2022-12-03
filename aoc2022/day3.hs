import Data.Char
import Data.Set (Set)
import Data.Set qualified as Set
import Functions

main = do
  input <- map parseStrSet . lines <$> readFile "input/day3.in"
  let alph = Set.fromList "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
      ansP1 = getPrio input alph 0
      ansP2 = getGroupCommon (map (uncurry Set.union) input) alph 0
  print ansP1
  print ansP2

getPrio :: [(Set Char, Set Char)] -> Set Char -> Integer -> Integer
getPrio [] a c = c
getPrio (x : xs) a c =
  let i = uncurry Set.intersection x
      id = Set.findIndex (head $ Set.toList i) a
   in if isUpper (head $ Set.toList i)
        then getPrio xs a (c + fromIntegral id + 26 + 1)
        else getPrio xs a (c + fromIntegral id - 26 + 1)

getGroupCommon :: [Set Char] -> Set Char -> Integer -> Integer
getGroupCommon [] a c = c
getGroupCommon (x : y : z : zs) a c =
  let i = foldl1 Set.intersection [x, y, z]
      id = Set.findIndex (head $ Set.toList i) a
   in if isUpper (head $ Set.toList i)
        then getGroupCommon zs a (c + fromIntegral id + 26 + 1)
        else getGroupCommon zs a (c + fromIntegral id - 26 + 1)
