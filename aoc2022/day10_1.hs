import Control.Monad
import Functions

main = do
  input <- words <$> readFile "input/day10.in"
  input' <- map (snd . parseMaybe) . lines <$> readFile "input/day10.in"
  -- let ansP1 = getSum (cycles input [(0, 1)])
  let c = cycles input [(1, 1)]
      c' = cyc input' [(1, 1)]
      l = [c !! 20, c !! 60, c !! 100, c !! 140, c !! 180, c !! 220]
      x = sum $ map (uncurry (*)) l
      asdf = filter (uncurry (==)) (zip c c')

  print input
  print x
  -- print ansP1
  print c
  print c'

-- getSum :: [(Int, Int)] -> Int
-- getSum l = sum $ map (uncurry (*)) (l)

cycles :: [String] -> [(Int, Int)] -> [(Int, Int)]
cycles [] c = c
cycles (x : xs) c = cycles xs (c ++ [(fst (last c) + 1, snd (last c) + g x)])
  where
    g "addx" = 0
    g "noop" = 0
    g n = if head n == '-' then negate (read (tail n)) else read n

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
