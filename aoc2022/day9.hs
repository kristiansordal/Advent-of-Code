import Data.List
import Data.Set (Set)
import Data.Set qualified as Set
import Functions

main = do
  input <- map parseCharNum . lines <$> readFile "input/day9.in"
  let ansP1 = rope input (0, 0) (0, 0) Set.empty
  -- let ansP2 = rope' input (replicate 10 (0, 0)) Set.empty
  print ansP1
  -- print ansP2
  rope' input (0, 0) (replicate 9 (0, 0)) Set.empty

type Move = (Char, Integer)

type Pos = (Integer, Integer)

rope :: [Move] -> Pos -> Pos -> Set Pos -> Int
rope [] h t s = length (Set.insert t s)
rope (x : xs) h t s
  | snd x == 0 = rope xs h (newPos h t) (Set.insert t s)
  | fst x == 'U' = rope ((fst x, snd x - 1) : xs) (fst h, snd h + 1) (newPos h t) (Set.insert t s)
  | fst x == 'D' = rope ((fst x, snd x - 1) : xs) (fst h, snd h - 1) (newPos h t) (Set.insert t s)
  | fst x == 'L' = rope ((fst x, snd x - 1) : xs) (fst h - 1, snd h) (newPos h t) (Set.insert t s)
  | fst x == 'R' = rope ((fst x, snd x - 1) : xs) (fst h + 1, snd h) (newPos h t) (Set.insert t s)

rope' :: [Move] -> Pos -> [Pos] -> Set Pos -> IO ()
rope' [] h k s = print $ length (Set.insert (last k) s)
rope' (x : xs) h k s
  | snd x == -1 = do
      print k
      rope' xs h (updatePos h k) (Set.insert (last k) s)
  | fst x == 'U' = do
      let h' = (fst h, snd h + 1)
       in rope' ((fst x, snd x - 1) : xs) h' (updatePos h' k) (Set.insert (last k) s)
  | fst x == 'D' = do
      let h' = (fst h, snd h - 1)
       in rope' ((fst x, snd x - 1) : xs) h' (updatePos h' k) (Set.insert (last k) s)
  | fst x == 'L' = do
      let h' = (fst h - 1, snd h)
       in rope' ((fst x, snd x - 1) : xs) h' (updatePos h' k) (Set.insert (last k) s)
  | fst x == 'R' = do
      let h' = (fst h + 1, snd h)
       in rope' ((fst x, snd x - 1) : xs) h' (updatePos h' k) (Set.insert (last k) s)

ropeState :: Pos -> Pos -> Pos
ropeState (x1, y1) (x2, y2) = (abs (x1 - x2), abs (y1 - y2))

updatePos :: Pos -> [Pos] -> [Pos]
updatePos p [] = []
updatePos p [x] = [newPos x p]
updatePos p (x : y : ys) = newPos p x : updatePos x (y : ys)

newPos :: Pos -> Pos -> Pos
newPos (x1, y1) (x2, y2)
  | (dx, dy) == (2, 2) = (x, y)
  | dx == 2 = (x, y1)
  | dy == 2 = (x1, y)
  | otherwise = (x2, y2)
  where
    (dx, dy) = ropeState (x1, y1) (x2, y2)
    x = if x1 > x2 then x1 - 1 else x1 + 1
    y = if y1 > y2 then y1 - 1 else y1 + 1
