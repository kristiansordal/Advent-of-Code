import Data.Map (Map)
import Data.Map qualified as Map
import Functions

main = do
  input <- map parseInt . lines <$> readFile "input/day20.in"
  -- let m = Map.fromList (zip input (tail input ++ [head input]))
  print (zip input (tail input ++ [head input]))
  mix (zip input [0 ..]) (zip input [0 ..]) (1, 0) 0

-- print m

-- let ansP1 = mix (zip input [0 ..]) (head input, 0) 0
-- print ansP1
-- mix (zip input [0 ..]) (head input, 0) 0

mix :: [(Int, Int)] -> [(Int, Int)] -> (Int, Int) -> Int -> IO ()
mix l orig next c
  | c == 6 = print l
  | otherwise = do
      (l', next'') <- move l next next'
      print (map fst l)
      -- print next'
      putStrLn $ "Moving: " ++ show next
      -- putStrLn $ "Next:   " ++ show next'
      putStrLn $ "Next:   " ++ show next''
      -- print (c + 1)
      print (map fst l')
      putStrLn "\n"
      mix l' orig next'' (c + 1)
  where
    next' = orig !! (c + 1)

-- (l', next'') = move l next next'

move :: [(Int, Int)] -> (Int, Int) -> (Int, Int) -> IO ([(Int, Int)], (Int, Int))
move l x next = do
  putStrLn $ "Before: " ++ show s
  putStrLn $ "After: " ++ show s'
  putStrLn $ "Index: " ++ show index
  return (l', next')
  where
    index = uncurry (+) x `mod` (length l - 1)
    (b, a) = splitAt (snd x) l
    (before, after) = splitAt (index + 1 - snd x) a
    l' = b ++ map (\(x, y) -> (x, y - 1)) (filter (/= x) before) ++ [(fst x, index)] ++ after
    (s, s') = splitAt (index + 1) l'
    next' = if index >= snd next then (fst next, snd next - 1) else next
