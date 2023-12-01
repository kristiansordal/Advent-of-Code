import Data.List.Extra
import Data.Map (Map)
import Data.Map qualified as Map
import Functions

main = do
  input <- map parseEither . lines <$> readFile "input/day21.in"
  print input

  -- let ansP1 = getRoot (Map.fromList input) "root"
  -- print ansP1
  getRoot (Map.fromList input) "root"

getRoot :: Map String (Either Integer String) -> String -> IO Integer
getRoot map key = case Map.lookup key map of
  Just val -> case val of
    Left num ->
      if key == "humn"
        then do
          print (num + 1000)
          return (num + 1000)
        else return num
    Right str ->
      let comps = splitOn " " str
       in do
            num1 <- getRoot map (head comps)
            num2 <- getRoot map (comps !! 2)
            ( if (key == "humn") || (key == "root")
                then
                  ( do
                      print num1
                      print num2
                      return $ eval num1 (comps !! 1) num2
                  )
                else return $ eval num1 (comps !! 1) num2
              )
  Nothing -> error ""

eval :: Integer -> String -> Integer -> Integer
eval x op y
  | op == "+" = x + y
  | op == "-" = x - y
  | op == "/" = x `div` y
  | op == "*" = x * y
