import Data.Maybe
import Functions

main = do
  input <- map (snd . parseMaybe) . lines <$> readFile "input/day10.in"
  let cycles = cyc input [(1, 1)]
      sum = getCycleSum cycles 0
      s = drawPixels cycles

  print sum
  putStrLn (head s)
  putStrLn (s !! 1)
  putStrLn (s !! 2)
  putStrLn (s !! 3)
  putStrLn (s !! 4)
  putStrLn (s !! 5)

drawPixels :: [(Int, Int)] -> [String]
drawPixels [] = []
drawPixels c = drawLine (map (\(x, y) -> (x `mod` 40, y `mod` 40)) (take 40 c)) 1 [0, 1, 2] "" : drawPixels (drop 40 c)

drawLine :: [(Int, Int)] -> Int -> [Int] -> String -> String
drawLine c 39 spr s = s
drawLine c n spr s
  | n `elem` spr = drawLine c (n + 1) spr' (s ++ "█")
  | otherwise = drawLine c (n + 1) spr' (s ++ " ")
  where
    d = snd $ c !! n
    spr' = [d, d + 1, d + 2]

getCycleSum :: [(Int, Int)] -> Int -> Int
getCycleSum c n
  | n > length c = 0
  | n == 20 = snd (c !! (n - 1)) * fst (c !! (n - 1)) + getCycleSum c (n + 40)
  | n `mod` 40 == 20 = snd (c !! (n - 1)) * fst (c !! (n - 1)) + getCycleSum c (n + 40)
  | otherwise = getCycleSum c (n + 20)

cyc :: [Maybe Int] -> [(Int, Int)] -> [(Int, Int)]
cyc [] c = c
cyc (x : xs) c =
  case x of
    (Just n) ->
      cyc
        xs
        ( c
            ++ [(fst (last c) + 1, snd $ last c)]
            ++ [(fst (last c) + 2, snd (last c) + n)]
        )
    Nothing -> cyc xs (c ++ [(fst (last c) + 1, snd $ last c)])
