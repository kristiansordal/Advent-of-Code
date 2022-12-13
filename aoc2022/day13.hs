import Data.Char
import Data.List.Extra
import Data.Maybe

main = do
  input <- map parsePacket . filter (not . null) . lines <$> readFile "input/day13.in"
  let (div1, div2) = (List [List [Lit 2]], List [List [Lit 6]])
  let sorted = sort $ div1 : div2 : input
  print $ sum . map fst . filter ((== True) . snd) . zip [1 ..] . map (\[a, b] -> a <= b) . chunksOf 2 $ input
  print (sorted !! fromMaybe 0 (elemIndex (parsePacket "[[2]]") sorted))
  print (sorted !! fromMaybe 0 (elemIndex (parsePacket "[[6]]") sorted))
  print ((fromMaybe 1 (elemIndex (parsePacket "[[2]]") sorted) + 1) * (fromMaybe 1 (elemIndex (parsePacket "[[6]]") sorted) + 1))

data Packet = List [Packet] | Lit Int
  deriving (Show, Read, Eq)

instance Ord Packet where
  compare (Lit a) (Lit b) = compare a b
  compare a@(Lit _) b@(List _) = compare (List [a]) b
  compare a@(List _) b@(Lit _) = compare a (List [b])
  compare (List xs) (List ys) = foldr (<>) (compare (length xs) (length ys)) (zipWith compare xs ys)

findDivider :: [Packet] -> Packet -> Integer
findDivider [] p' = 0
findDivider (p : ps) p'
  | p == p' = 0
  | otherwise = findDivider ps p' + 1

parsePacket :: String -> Packet
parsePacket = read . parse
  where
    parse [] = ""
    parse ('[' : xs) = "List [" ++ parse xs
    parse (x : xs)
      | isDigit x = "Lit " ++ (x : takeWhile isDigit xs) ++ parse (dropWhile isDigit xs)
      | otherwise = x : parse xs
