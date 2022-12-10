import Control.Concurrent (threadDelay)
import Data.List.Split
import Data.Maybe
import Functions
import System.Console.ANSI

main = do
  input <- map (snd . parseMaybe) . lines <$> readFile "input/day10.in"
  let cycles = cyc input [(1, 1)]
      sum = cycSum cycles 0
      s = drawPixels cycles

  print sum
  mapM_ printWithDelay (take 6 s)

printWithDelay :: String -> IO ()
printWithDelay [] = return ()
printWithDelay (c : cs) = do
  putStr $ "\ESC[92m" ++ [c]
  threadDelay 20000
  printWithDelay cs

drawPixels :: [(Int, Int)] -> [String]
drawPixels c = map (\ys -> drawLine (map (\(x, y) -> (x `mod` 40, y `mod` 40)) (take 40 ys)) 1 [0, 1, 2] "") (chunksOf 40 c)

drawLine :: [(Int, Int)] -> Int -> [Int] -> String -> String
drawLine c n spr s
  | n == 39 = s ++ "\n"
  | n `elem` spr = drawLine c (n + 1) spr' (s ++ "█")
  | otherwise = drawLine c (n + 1) spr' (s ++ " ")
  where
    d = snd $ c !! n
    spr' = [d, d + 1, d + 2]

cycSum :: [(Int, Int)] -> Int -> Int
cycSum c n
  | n > length c = 0
  | n == 20 = snd (c !! (n - 1)) * fst (c !! (n - 1)) + cycSum c (n + 40)
  | n `mod` 40 == 20 = snd (c !! (n - 1)) * fst (c !! (n - 1)) + cycSum c (n + 40)
  | otherwise = cycSum c (n + 20)

cyc :: [Maybe Int] -> [(Int, Int)] -> [(Int, Int)]
cyc [] c = c
cyc (x : xs) c =
  case x of
    (Just n) -> cyc xs (c ++ [cyc1] ++ [cyc2])
      where
        cyc2 = (fst (last c) + 2, snd (last c) + n)
    Nothing -> cyc xs (c ++ [cyc1])
  where
    cyc1 = (fst (last c) + 1, snd $ last c)
