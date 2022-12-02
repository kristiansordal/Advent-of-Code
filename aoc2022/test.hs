import Functions

main = do
  input <- map parseNumWord . lines <$> readFile "test.in"
  print input
