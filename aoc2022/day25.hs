main = do
  input <- lines <$> readFile "input/day25.in"
  print (toSnafu (sum $ map (`fromSnafu` 0) input) "")

fromSnafu :: String -> Int -> Int
fromSnafu [] acc = acc
fromSnafu (x : xs) acc
  | x == '2' = fromSnafu xs (acc + 2 * (5 ^ pos))
  | x == '1' = fromSnafu xs (acc + (5 ^ pos))
  | x == '0' = fromSnafu xs acc
  | x == '-' = fromSnafu xs (acc - (5 ^ pos))
  | x == '=' = fromSnafu xs (acc - 2 * (5 ^ pos))
  where
    pos = length (x : xs) - 1

toSnafu :: Int -> String -> String
toSnafu 0 str = reverse str
toSnafu num str
  | rem == 0 = toSnafu n (str ++ "0")
  | rem == 1 = toSnafu n (str ++ "1")
  | rem == 2 = toSnafu n (str ++ "2")
  | rem == -1 = toSnafu n (str ++ "-")
  | rem == -2 = toSnafu n (str ++ "=")
  | otherwise = error "Wrong remainder"
  where
    rem | num `mod` 5 == 3 = -2 | num `mod` 5 == 4 = -1 | otherwise = num `mod` 5
    n | num `mod` 5 == 3 || num `mod` 5 == 4 = num `div` 5 + 1 | otherwise = num `div` 5
