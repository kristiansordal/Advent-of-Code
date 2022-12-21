import Data.List.Extra
import Data.Map (Map)
import Data.Map qualified as Map
import Functions
import Text.Read

main = do
  input <- map parse . lines <$> readFile "input/day21.in"
  let ansP1 = getRoot (Map.fromList input) "root"
  print ansP1

getRoot :: Map String (Either Integer String) -> String -> Integer
getRoot map key = case Map.lookup key map of
  Just val -> case val of
    Left num -> num
    Right str ->
      let comps = splitOn " " str
       in eval (getRoot map (head comps)) (comps !! 1) (getRoot map (comps !! 2))
  Nothing -> error "asf"

eval :: Integer -> String -> Integer -> Integer
eval x op y
  | op == "+" = x + y
  | op == "-" = x - y
  | op == "/" = x `div` y
  | op == "*" = x * y

parse :: String -> (String, Either Integer String)
parse s = (key, val')
  where
    [key, val] = splitOn ": " s
    val' = case readMaybe val of
      (Just num) -> Left num
      Nothing -> Right val
