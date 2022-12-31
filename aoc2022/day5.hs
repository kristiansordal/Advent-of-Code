import Functions

main = do
  stack <- lines <$> readFile "input/day5_1.in"
  moves <- map parseList . lines <$> readFile "input/day5.in"
  let ansP1 = moveCrates stack moves moveCrateOne
  let ansP2 = moveCrates stack moves moveCrateAll
  putStrLn ansP1
  putStrLn ansP2

type Crates = [String]

type Move = [[Integer]]

moveCrates :: (Integral a) => [[b]] -> [[a]] -> ([b] -> [b] -> a -> ([b], [b])) -> [b]
moveCrates cs [] fun = map head cs
moveCrates cs (y : ys) fun =
  let f = cs !! (fromIntegral (y !! 1) - 1)
      t = cs !! (fromIntegral (y !! 2) - 1)
      newStack = fun f t (head y)
      crates = splitAt (fromIntegral (y !! 1) - 1) cs
      crates' = fst crates ++ fst newStack : drop 1 (snd crates)
      crates'' = splitAt (fromIntegral (y !! 2) - 1) crates'
      crates''' = fst crates'' ++ snd newStack : drop 1 (snd crates'')
   in moveCrates crates''' ys fun

moveCrateOne :: (Eq t, Num t) => [a] -> [a] -> t -> ([a], [a])
moveCrateOne x y 0 = (x, y)
moveCrateOne x y n = moveCrateOne (tail x) (head x : y) (n - 1)

moveCrateAll :: (Integral t) => [a] -> [a] -> t -> ([a], [a])
moveCrateAll x y n = (drop (fromIntegral n) x, take (fromIntegral n) x ++ y)
